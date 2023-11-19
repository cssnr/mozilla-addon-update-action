# Mozilla Addon Update File Action

Update the Mozilla Firefox Update JSON File after a Release.

For more details see: [action.yaml](action.yaml)

_Coming Soon..._

## Inputs

| input    | default       | description                                |
|----------|---------------|--------------------------------------------|
| url      | -             | Update URL with `{version}` in the string. |
| manifest | manifest.json | Manifest File Location                     |
| update   | update.json   | Update File Location                       |
| addon_id | None          | Mozilla Addon ID (if not in manifest.json) |

## Short Example

```yaml
name: 'Mozilla Addon Update'

on:
  push:

jobs:
  mozilla-update:
    name: 'Mozilla Addon Update'
    runs-on: ubuntu-latest
    timeout-minutes: 5

    steps:
      - name: 'Mozilla Addon Update'
        uses: cssnr/mozilla-addon-update-action@master
        with:
          url: 'https://github.com/cssnr/link-extractor/releases/download/{version}/link_extractor-firefox.xpi'
          manifest: manifest.json
          update: update.json
          addon_id: link-extractor@cssnr.com
```

## Full Example

```yaml
name: 'Mozilla Addon Update'

on:
  push:

jobs:
  mozilla-update:
    name: 'Mozilla Addon Update'
    runs-on: ubuntu-latest
    timeout-minutes: 5

    steps:
      - name: 'Checkout'
        uses: actions/checkout@v3

      - name: "Mozilla Addon Update"
        uses: cssnr/mozilla-addon-update-action@master
        with:
          url: 'https://github.com/cssnr/link-extractor/releases/download/{version}/link_extractor-firefox.xpi'
          manifest: manifest.json
          update: update.json
          addon_id: link-extractor@cssnr.com

      - name: 'Commit files'
        run: |
          git config --local user.email "41898282+github-actions[bot]@users.noreply.github.com"
          git config --local user.name "github-actions[bot]"
          git commit -a -m "Update update.json"

      - name: 'Push changes'
        uses: ad-m/github-push-action@master
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          branch: master
```

To see this used in a build/publish/update workflow, see: https://github.com/cssnr/aviation-tools/blob/master/.github/workflows/build.yaml
