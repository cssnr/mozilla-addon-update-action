[![GitHub Tag Major](https://img.shields.io/github/v/tag/cssnr/mozilla-addon-update-action?sort=semver&filter=!v*.*&logo=git&logoColor=white&labelColor=585858&label=%20)](https://github.com/cssnr/mozilla-addon-update-action/tags)
[![GitHub Tag Minor](https://img.shields.io/github/v/tag/cssnr/mozilla-addon-update-action?sort=semver&filter=!v*.*.*&logo=git&logoColor=white&labelColor=585858&label=%20)](https://github.com/cssnr/mozilla-addon-update-action/releases)
[![GitHub Release Version](https://img.shields.io/github/v/release/cssnr/mozilla-addon-update-action?logo=git&logoColor=white&labelColor=585858&label=%20)](https://github.com/cssnr/mozilla-addon-update-action/releases/latest)
[![Workflow Release](https://img.shields.io/github/actions/workflow/status/cssnr/mozilla-addon-update-action/release.yaml?logo=cachet&label=release)](https://github.com/cssnr/mozilla-addon-update-action/actions/workflows/release.yaml)
[![Workflow Test](https://img.shields.io/github/actions/workflow/status/cssnr/mozilla-addon-update-action/test.yaml?logo=cachet&label=test)](https://github.com/cssnr/mozilla-addon-update-action/actions/workflows/test.yaml)
[![Workflow Lint](https://img.shields.io/github/actions/workflow/status/cssnr/mozilla-addon-update-action/lint.yaml?logo=cachet&label=lint)](https://github.com/cssnr/mozilla-addon-update-action/actions/workflows/lint.yaml)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=cssnr_mozilla-addon-update-action&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=cssnr_mozilla-addon-update-action)
[![GitHub Last Commit](https://img.shields.io/github/last-commit/cssnr/mozilla-addon-update-action?logo=github&label=updated)](https://github.com/cssnr/mozilla-addon-update-action/pulse)
[![Codeberg Last Commit](https://img.shields.io/gitea/last-commit/cssnr/mozilla-addon-update-action/master?gitea_url=https%3A%2F%2Fcodeberg.org%2F&logo=codeberg&logoColor=white&label=updated)](https://codeberg.org/cssnr/mozilla-addon-update-action)
[![GitHub Contributors](https://img.shields.io/github/contributors/cssnr/mozilla-addon-update-action?logo=github)](https://github.com/cssnr/mozilla-addon-update-action/graphs/contributors)
[![GitHub Repo Size](https://img.shields.io/github/repo-size/cssnr/mozilla-addon-update-action?logo=bookstack&logoColor=white&label=repo%20size)](https://github.com/cssnr/mozilla-addon-update-action?tab=readme-ov-file#readme)
[![GitHub Top Language](https://img.shields.io/github/languages/top/cssnr/mozilla-addon-update-action?logo=htmx)](https://github.com/cssnr/mozilla-addon-update-action)
[![GitHub Forks](https://img.shields.io/github/forks/cssnr/mozilla-addon-update-action?style=flat&logo=github)](https://github.com/cssnr/mozilla-addon-update-action/forks)
[![GitHub Discussions](https://img.shields.io/github/discussions/cssnr/mozilla-addon-update-action?logo=github)](https://github.com/cssnr/mozilla-addon-update-action/discussions)
[![GitHub Repo Stars](https://img.shields.io/github/stars/cssnr/mozilla-addon-update-action?style=flat&logo=github)](https://github.com/cssnr/mozilla-addon-update-action/stargazers)
[![GitHub Org Stars](https://img.shields.io/github/stars/cssnr?style=flat&logo=github&label=org%20stars)](https://cssnr.github.io/)
[![Discord](https://img.shields.io/discord/899171661457293343?logo=discord&logoColor=white&label=discord&color=7289da)](https://discord.gg/wXy6m2X8wY)
[![Ko-fi](https://img.shields.io/badge/Ko--fi-72a5f2?logo=kofi&label=support)](https://ko-fi.com/cssnr)

# Mozilla Addon Update Action

- [Inputs](#Inputs)
- [Outputs](#Outputs)
- [Notes](#Notes)
- [Examples](#Examples)
- [Support](#Support)
- [Contributing](#Contributing)

Update the Mozilla Firefox Update JSON File after a Release for Self Hosted Extensions.

## Inputs

| input    | required | default         | description                                |
| -------- | :------: | --------------- | ------------------------------------------ |
| url      | **Yes**  | -               | Update URL with `{version}` in the string. |
| update   |    -     | `update.json`   | Update JSON File Location                  |
| manifest |    -     | `manifest.json` | \* Manifest File Location                  |
| version  |    -     | -               | \* Override Version from `manifest`        |
| addon_id |    -     | -               | \* Override Addon ID from `manifest`       |

**manifest** - If provided the `version` and `addon_id` will be parsed from this file.

**version** - Manually specify the `version` to use for `{version}` in `url`.

**addon_id** - Manually specify the `addon_id` to use for `update` JSON file.
If not provided this is parsed from the `manfiest` key: `browser_specific_settings.gecko.id`

```yaml
- name: 'Mozilla Addon Update'
  uses: cssnr/mozilla-addon-update-action@v1
  with:
    url: 'https://github.com/cssnr/link-extractor/releases/download/{version}/link_extractor-firefox.xpi'
```

## Outputs

| output | description        |
| ------ | ------------------ |
| url    | Update URL Result  |
| result | Update JSON Result |

```yaml
- name: 'Mozilla Addon Update'
  id: update
  uses: cssnr/mozilla-addon-update-action@v1
  with:
    url: 'https://github.com/cssnr/link-extractor/releases/download/{version}/link_extractor-firefox.xpi'

- name: 'Echo Outputs'
  run: |
    echo '${{ steps.update.outputs.url }}'
    echo '${{ steps.update.outputs.result }}'
```

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
- name: 'Mozilla Addon Update'
  uses: cssnr/mozilla-addon-update-action@v1
  with:
    url: 'https://github.com/cssnr/link-extractor/releases/download/{version}/link_extractor-firefox.xpi'
    update: update.json
    manifest: manifest.json
    version: '1.0.0'
    addon_id: link-extractor@cssnr.com
```

Simple Example:

```yaml
name: 'Mozilla Addon Update'

on:
  workflow_dispatch:
  release:
    types: [published]

jobs:
  mozilla-update:
    name: 'Mozilla Addon Update'
    runs-on: ubuntu-latest
    timeout-minutes: 5
    if: ${{ github.event_name == 'release' }}

    steps:
      - name: 'Checkout'
        uses: actions/checkout@v4

      - name: 'Mozilla Addon Update'
        uses: cssnr/mozilla-addon-update-action@v1
        with:
          url: 'https://github.com/cssnr/link-extractor/releases/download/{version}/link_extractor-firefox.xpi'
```

Full Example:

```yaml
name: 'Mozilla Addon Update'

on:
  workflow_dispatch:
  release:
    types: [published]

jobs:
  build:
    name: 'Build'
    runs-on: ubuntu-latest
    timeout-minutes: 5

    steps:
      - name: 'Checkout'
        uses: actions/checkout@v4

      - name: 'Build All'
        run: |-
          npm install
          npm run build

      - name: 'Upload to Release'
        uses: svenstaro/upload-release-action@v2
        with:
          repo_token: ${{ secrets.GITHUB_TOKEN }}
          file: web-ext-artifacts/*
          tag: ${{ github.ref }}
          overwrite: true
          file_glob: true

  mozilla-update:
    name: 'Mozilla Addon Update'
    runs-on: ubuntu-latest
    timeout-minutes: 5
    needs: [build]
    if: ${{ github.event_name == 'release' }}

    steps:
      - name: 'Checkout'
        uses: actions/checkout@v4

      - name: 'Mozilla Addon Update'
        uses: cssnr/mozilla-addon-update-action@v1
        with:
          url: 'https://github.com/cssnr/link-extractor/releases/download/{version}/link_extractor-firefox.xpi'

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

To see this used in a build/publish/update workflow, check out:  
https://github.com/cssnr/aviation-tools/blob/master/.github/workflows/build.yaml

# Support

For general help or to request a feature see:

- Q&A Discussion: https://github.com/cssnr/mozilla-addon-update-action/discussions/categories/q-a
- Request a Feature: https://github.com/cssnr/mozilla-addon-update-action/discussions/categories/feature-requests

If you are experiencing an issue/bug or getting unexpected results you can:

- Report an Issue: https://github.com/cssnr/mozilla-addon-update-action/issues
- Chat with us on Discord: https://discord.gg/wXy6m2X8wY
- Provide General Feedback: [https://cssnr.github.io/feedback/](https://cssnr.github.io/feedback/?app=Mozilla%20Addon%20Update)

For more information, see the CSSNR [SUPPORT.md](https://github.com/cssnr/.github/blob/master/.github/SUPPORT.md#support).

# Contributing

Please consider making a donation to support the development of this project
and [additional](https://cssnr.com/) open source projects.

[![Ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/cssnr)

If you would like to submit a PR, please review the [CONTRIBUTING.md](#contributing-ov-file).

Additionally, you can support other GitHub Actions I have published:

- [Stack Deploy Action](https://github.com/cssnr/stack-deploy-action?tab=readme-ov-file#readme)
- [Portainer Stack Deploy](https://github.com/cssnr/portainer-stack-deploy-action?tab=readme-ov-file#readme)
- [VirusTotal Action](https://github.com/cssnr/virustotal-action?tab=readme-ov-file#readme)
- [Mirror Repository Action](https://github.com/cssnr/mirror-repository-action?tab=readme-ov-file#readme)
- [Update Version Tags Action](https://github.com/cssnr/update-version-tags-action?tab=readme-ov-file#readme)
- [Update JSON Value Action](https://github.com/cssnr/update-json-value-action?tab=readme-ov-file#readme)
- [Parse Issue Form Action](https://github.com/cssnr/parse-issue-form-action?tab=readme-ov-file#readme)
- [Cloudflare Purge Cache Action](https://github.com/cssnr/cloudflare-purge-cache-action?tab=readme-ov-file#readme)
- [Mozilla Addon Update Action](https://github.com/cssnr/mozilla-addon-update-action?tab=readme-ov-file#readme)
- [Docker Tags Action](https://github.com/cssnr/docker-tags-action?tab=readme-ov-file#readme)
- [Package Changelog Action](https://github.com/cssnr/package-changelog-action?tab=readme-ov-file#readme)
- [NPM Outdated Check Action](https://github.com/cssnr/npm-outdated-action?tab=readme-ov-file#readme)
- [Label Creator Action](https://github.com/cssnr/label-creator-action?tab=readme-ov-file#readme)
- [Algolia Crawler Action](https://github.com/cssnr/algolia-crawler-action?tab=readme-ov-file#readme)
- [Upload Release Action](https://github.com/cssnr/upload-release-action?tab=readme-ov-file#readme)

For a full list of current projects visit: [https://cssnr.github.io/](https://cssnr.github.io/)
