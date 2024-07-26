[![Tags](https://img.shields.io/github/actions/workflow/status/cssnr/mozilla-addon-update-action/tags.yaml?logo=github&logoColor=white&label=tags)](https://github.com/cssnr/mozilla-addon-update-action/actions/workflows/tags.yaml)
[![Test](https://img.shields.io/github/actions/workflow/status/cssnr/mozilla-addon-update-action/test.yaml?logo=github&logoColor=white&label=test)](https://github.com/cssnr/mozilla-addon-update-action/actions/workflows/test.yaml)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=cssnr_mozilla-addon-update-action&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=cssnr_mozilla-addon-update-action)
[![GitHub Release Version](https://img.shields.io/github/v/release/cssnr/mozilla-addon-update-action?logo=github)](https://github.com/cssnr/mozilla-addon-update-action/releases/latest)
[![GitHub Last Commit](https://img.shields.io/github/last-commit/cssnr/parse-issue-form-action?logo=github&logoColor=white&label=updated)](https://github.com/cssnr/parse-issue-form-action/graphs/commit-activity)
[![GitHub Top Language](https://img.shields.io/github/languages/top/cssnr/mozilla-addon-update-action?logo=htmx&logoColor=white)](https://github.com/cssnr/mozilla-addon-update-action)
[![GitHub Org Stars](https://img.shields.io/github/stars/cssnr?style=flat&logo=github&logoColor=white)](https://cssnr.github.io/)
[![Discord](https://img.shields.io/discord/899171661457293343?logo=discord&logoColor=white&label=discord&color=7289da)](https://discord.gg/wXy6m2X8wY)

# Mozilla Addon Update Action

Update the Mozilla Firefox Update JSON File after a Release for Self Hosted Extensions.

* [Inputs](#Inputs)
* [Outputs](#Outputs)
* [Notes](#Notes)
* [Examples](#Examples)
* [Support](#Support)
* [Contributing](#Contributing)

## Inputs

| input    | required | default         | description                                |
|----------|----------|-----------------|--------------------------------------------|
| url      | **Yes**  | -               | Update URL with `{version}` in the string. |
| update   | No       | `update.json`   | Update JSON File Location                  |
| manifest | No       | `manifest.json` | Manifest File Location *                   |
| version  | No       | -               | Override Version from `manifest` *         |
| addon_id | No       | -               | Override Addon ID from `manifest` *        |

**manifest** - If provided the `version` and `addon_id` will be parsed from this file.

**version** - Manually specify the `version` to use for `{version}` in `url`.

**addon_id** - Manually specify the `addon_id` to use for `update` JSON file. If not provided this is parsed from
the `manfiest` key: `browser_specific_settings.gecko.id`

```yaml
  - name: "Mozilla Addon Update"
    uses: cssnr/mozilla-addon-update-action@v1
    with:
      url: "https://github.com/cssnr/link-extractor/releases/download/{version}/link_extractor-firefox.xpi"
```

## Outputs

| output | description        |
|--------|--------------------|
| url    | Update URL Result  |
| result | Update JSON Result |

## Notes

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

For more details see: [src/main.py](src/main.py).

Mozilla Documentation: https://extensionworkshop.com/documentation/manage/updating-your-extension/

## Examples

Basic Example with All Inputs:

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

Use Outputs:

```yaml
  - name: "Mozilla Addon Update"
    id: update
    uses: cssnr/mozilla-addon-update-action@v1
    with:
      url: "https://github.com/cssnr/link-extractor/releases/download/{version}/link_extractor-firefox.xpi"
      update: update.json
      manifest: manifest.json
      version: "1.0.0"
      addon_id: link-extractor@cssnr.com

  - name: "Echo Outputs"
    run: |
      echo '${{ steps.update.outputs.url }}'
      echo '${{ steps.update.outputs.result }}'

```

Simple Example:

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
```

Full Example:

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

# Support

For general help or to request a feature see:

- Q&A Discussion: https://github.com/cssnr/virustotal-action/discussions/categories/q-a
- Request a Feature: https://github.com/cssnr/virustotal-action/discussions/categories/feature-requests

If you are experiencing an issue/bug or getting unexpected results you can:

- Report an Issue: https://github.com/cssnr/virustotal-action/issues
- Chat with us on Discord: https://discord.gg/wXy6m2X8wY
- Provide General
  Feedback: [https://cssnr.github.io/feedback/](https://cssnr.github.io/feedback/?app=Mozilla%20Addon%20Update)

# Contributing

Currently, the best way to contribute to this project is to star this project on GitHub.

Additionally, you can support other GitHub Actions I have published:

- [VirusTotal Action](https://github.com/cssnr/virustotal-action)
- [Update Version Tags Action](https://github.com/cssnr/update-version-tags-action)
- [Update JSON Value Action](https://github.com/cssnr/update-json-value-action)
- [Parse Issue Form Action](https://github.com/cssnr/parse-issue-form-action)
- [Portainer Stack Deploy](https://github.com/cssnr/portainer-stack-deploy-action)
- [Mozilla Addon Update Action](https://github.com/cssnr/mozilla-addon-update-action)

For a full list of current projects to support visit: [https://cssnr.github.io/](https://cssnr.github.io/)
