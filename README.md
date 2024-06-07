[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=cssnr_mozilla-addon-update-action&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=cssnr_mozilla-addon-update-action)
[![Tags](https://github.com/cssnr/mozilla-addon-update-action/actions/workflows/tags.yaml/badge.svg)](https://github.com/cssnr/mozilla-addon-update-action/actions/workflows/tags.yaml)
# Mozilla Addon Update Action

Update the Mozilla Firefox Update JSON File after a Release for Self Hosted Extensions.

For more details see: [action.yaml](action.yaml) and [update-json.py](src/update-json.py).

Documentation: https://extensionworkshop.com/documentation/manage/updating-your-extension/

## Inputs

| input    | required | default       | description                                |
|----------|----------|---------------|--------------------------------------------|
| url      | Yes      | -             | Update URL with `{version}` in the string. |
| update   | No       | update.json   | Update JSON File Location                  |
| manifest | No       | manifest.json | Manifest File Location                     |
| version  | No*      | -             | Version (overrides manifest version)       |
| addon_id | No*      | -             | Addon ID (overrides manifest id)           |

> [!NOTE]  
> If you provide the `manifest` both `version` and `addon_id` will be parsed if present.  
> Otherwise, you must provide both the `version` and `addon_id` which take precedence over `manifest`.

```yaml
  - name: "Mozilla Addon Update"
    uses: cssnr/mozilla-addon-update-action@v1
    with:
      url: "https://github.com/cssnr/link-extractor/releases/download/{version}/link_extractor-firefox.xpi"
      update: update.json
      manifest: manifest.json
      version: "1.0.0"
      addon_id: link-extractor@cssnr.com
```

## More Information

This action expects the `input_update` JSON file to exist, be valid JSON and have a matching addon_id entry.
At a minimum, add a file similar to this where `link-extractor@cssnr.com` is your Addon ID:

```json
{
    "addons": {
        "link-extractor@cssnr.com": {
            "updates": []
        }
    }
}
```

## Short Example

```yaml
name: "Mozilla Addon Update"

on:
  workflow_dispatch:
  release:
    types: [ published ]

jobs:
  mozilla-update:
    name: "Mozilla Addon Update"
    runs-on: ubuntu-latest
    timeout-minutes: 5
    if: ${{ github.event_name == 'release' }}

    steps:
      - name: "Checkout"
        uses: actions/checkout@v4

      - name: "Mozilla Addon Update"
        uses: cssnr/mozilla-addon-update-action@v1
        with:
          url: "https://github.com/cssnr/link-extractor/releases/download/{version}/link_extractor-firefox.xpi"
          update: update.json
          manifest: manifest.json
          version: "1.0.0"
          addon_id: link-extractor@cssnr.com
```

## Full Example

```yaml
name: "Mozilla Addon Update"

on:
  workflow_dispatch:
  release:
    types: [ published ]

jobs:
  build:
    name: "Build"
    runs-on: ubuntu-latest
    timeout-minutes: 5

    steps:
      - name: "Checkout"
        uses: actions/checkout@v4

      - name: "Build All"
        run: |-
          npm install
          npm run build

      - name: "Upload to Release"
        uses: svenstaro/upload-release-action@v2
        with:
          repo_token: ${{ secrets.GITHUB_TOKEN }}
          file: web-ext-artifacts/*
          tag: ${{ github.ref }}
          overwrite: true
          file_glob: true

  mozilla-update:
    name: "Mozilla Addon Update"
    runs-on: ubuntu-latest
    timeout-minutes: 5
    needs: [ build ]
    if: ${{ github.event_name == 'release' }}

    steps:
      - name: "Checkout"
        uses: actions/checkout@v4

      - name: "Mozilla Addon Update"
        uses: cssnr/mozilla-addon-update-action@v1
        with:
          url: "https://github.com/cssnr/link-extractor/releases/download/{version}/link_extractor-firefox.xpi"
          update: update.json
          manifest: manifest.json
          version: "1.0.0"
          addon_id: link-extractor@cssnr.com

      - name: "Commit files"
        run: |
          git config --local user.email "41898282+github-actions[bot]@users.noreply.github.com"
          git config --local user.name "github-actions[bot]"
          git commit -a -m "Update update.json"

      - name: "Push changes"
        uses: ad-m/github-push-action@master
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          branch: master
```

To see this used in a build/publish/update workflow, check out:  
https://github.com/cssnr/aviation-tools/blob/master/.github/workflows/build.yaml
