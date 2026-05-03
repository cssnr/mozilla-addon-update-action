[![GitHub Tag Major](https://img.shields.io/github/v/tag/cssnr/mozilla-addon-update-action?sort=semver&filter=!v*.*&logo=git&logoColor=white&labelColor=585858&label=%20)](https://github.com/cssnr/mozilla-addon-update-action/tags)
[![GitHub Tag Minor](https://img.shields.io/github/v/tag/cssnr/mozilla-addon-update-action?sort=semver&filter=!v*.*.*&logo=git&logoColor=white&labelColor=585858&label=%20)](https://github.com/cssnr/mozilla-addon-update-action/releases)
[![GitHub Release Version](https://img.shields.io/github/v/release/cssnr/mozilla-addon-update-action?logo=git&logoColor=white&labelColor=585858&label=%20)](https://github.com/cssnr/mozilla-addon-update-action/releases/latest)
[![Action Run Using](https://img.shields.io/badge/dynamic/yaml?url=https%3A%2F%2Fraw.githubusercontent.com%2Fcssnr%2Fmozilla-addon-update-action%2Frefs%2Fheads%2Fmaster%2Faction.yml&query=%24.runs.using&logo=githubactions&logoColor=white&label=runs)](https://github.com/cssnr/mozilla-addon-update-action/blob/master/action.yml)
[![Workflow Release](https://img.shields.io/github/actions/workflow/status/cssnr/mozilla-addon-update-action/release.yaml?logo=norton&logoColor=white&label=release)](https://github.com/cssnr/mozilla-addon-update-action/actions/workflows/release.yaml)
[![Workflow Test](https://img.shields.io/github/actions/workflow/status/cssnr/mozilla-addon-update-action/test.yaml?logo=norton&logoColor=white&label=test)](https://github.com/cssnr/mozilla-addon-update-action/actions/workflows/test.yaml)
[![Workflow Lint](https://img.shields.io/github/actions/workflow/status/cssnr/mozilla-addon-update-action/lint.yaml?logo=norton&logoColor=white&label=lint)](https://github.com/cssnr/mozilla-addon-update-action/actions/workflows/lint.yaml)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=cssnr_mozilla-addon-update-action&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=cssnr_mozilla-addon-update-action)
[![GitHub Last Commit](https://img.shields.io/github/last-commit/cssnr/mozilla-addon-update-action?logo=github&label=updated)](https://github.com/cssnr/mozilla-addon-update-action)
[![Codeberg Last Commit](https://img.shields.io/gitea/last-commit/cssnr/mozilla-addon-update-action/master?gitea_url=https%3A%2F%2Fcodeberg.org%2F&logo=codeberg&logoColor=white&label=updated)](https://codeberg.org/cssnr/mozilla-addon-update-action)
[![GitHub Repo Size](https://img.shields.io/github/repo-size/cssnr/mozilla-addon-update-action?logo=buffer&label=repo%20size)](https://github.com/cssnr/mozilla-addon-update-action?tab=readme-ov-file#readme)
[![GitHub Top Language](https://img.shields.io/github/languages/top/cssnr/mozilla-addon-update-action?logo=devbox)](https://github.com/cssnr/mozilla-addon-update-action?tab=readme-ov-file#readme)
[![GitHub Contributors](https://img.shields.io/github/contributors-anon/cssnr/mozilla-addon-update-action?logo=southwestairlines)](https://github.com/cssnr/mozilla-addon-update-action/graphs/contributors)
[![GitHub Issues](https://img.shields.io/github/issues/cssnr/mozilla-addon-update-action?logo=codeforces&logoColor=white)](https://github.com/cssnr/mozilla-addon-update-action/issues)
[![GitHub Discussions](https://img.shields.io/github/discussions/cssnr/mozilla-addon-update-action?logo=livechat&logoColor=white)](https://github.com/cssnr/mozilla-addon-update-action/discussions)
[![GitHub Forks](https://img.shields.io/github/forks/cssnr/mozilla-addon-update-action?style=flat&logo=forgejo&logoColor=white)](https://github.com/cssnr/mozilla-addon-update-action/forks)
[![GitHub Repo Stars](https://img.shields.io/github/stars/cssnr/mozilla-addon-update-action?style=flat&logo=gleam&logoColor=white)](https://github.com/cssnr/mozilla-addon-update-action/stargazers)
[![GitHub Org Stars](https://img.shields.io/github/stars/cssnr?style=flat&logo=apachespark&logoColor=white&label=org%20stars)](https://cssnr.github.io/)
[![Discord](https://img.shields.io/discord/899171661457293343?logo=discord&logoColor=white&label=discord&color=7289da)](https://discord.gg/wXy6m2X8wY)
[![Ko-fi](https://img.shields.io/badge/Ko--fi-72a5f2?logo=kofi&label=support)](https://ko-fi.com/cssnr)

# Mozilla Addon Update Action

<a title="Mozilla Addon Update Action" href="https://actions.cssnr.com/" target="_blank">
<img alt="Mozilla Addon Update Action" align="right" width="128" height="auto" src="https://raw.githubusercontent.com/cssnr/mozilla-addon-update-action/master/.github/assets/logo.svg"></a>

- [Inputs](#Inputs)
- [Outputs](#Outputs)
- [Notes](#Notes)
- [Examples](#Examples)
- [Tags](#Tags)
- [Support](#Support)
- [Contributing](#Contributing)

Update the Mozilla Firefox Update JSON File after a Release for Self Hosted Extensions.

## Inputs

| Input    | Default         | Short&nbsp;Description&nbsp;of&nbsp;the&nbsp;Input&nbsp;Value |
| -------- | --------------- | ------------------------------------------------------------- |
| url      | **Required**    | Update URL w/ `{version}` Template                            |
| update   | `update.json`   | Update JSON File Location                                     |
| manifest | `manifest.json` | \* Manifest File Location                                     |
| version  | -               | \* Override Version from `manifest`                           |
| addon_id | -               | \* Override Addon ID from `manifest`                          |

**url** - You can provide a fully formatted URL or use the `{version}` template string.

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

| Output | Description        |
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

> [!TIP]  
> The addon will now attempt to create the file if it does not exist.

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
        uses: actions/checkout@v6

      - name: 'Mozilla Addon Update'
        uses: cssnr/mozilla-addon-update-action@v1
        with:
          url: 'https://github.com/cssnr/link-extractor/releases/download/{version}/link_extractor-firefox.xpi'
```

Full Example:

```yaml
name: 'Release'

on:
  release:
    types: [published]

env:
  PACKAGE_NAME: geoimage
  MOZILLA_ID: geo-image@cssnr.com
  UPDATE_JSON: update.json

jobs:
  build:
    name: 'Build'
    uses: ./.github/workflows/build.yaml
    secrets: inherit
    with:
      version: ${{ github.event.release.tag_name }} # github.ref_name can be empty
    permissions:
      contents: write

  publish-mozilla:
    # https://mozilla.github.io/addons-server/topics/api/index.html
    name: 'Publish Mozilla'
    if: ${{ !github.event.release.prerelease }}
    runs-on: ubuntu-latest
    timeout-minutes: 15
    needs: [build]

    permissions:
      contents: write

    environment:
      name: mozilla
      url: '${{ github.server_url }}/${{ github.repository }}/releases/latest/download/${{ env.PACKAGE_NAME }}-firefox.xpi'

    steps:
      - name: 'Download Artifacts'
        uses: actions/download-artifact@v8
        with:
          name: artifacts

      # NOTE: This installs web-ext using npx
      - name: 'Sign Mozilla Addon'
        # https://extensionworkshop.com/documentation/develop/web-ext-command-reference/#web-ext-sign
        env:
          FIREFOX_API_KEY: ${{ secrets.FIREFOX_API_KEY }}
          FIREFOX_API_SECRET: ${{ secrets.FIREFOX_API_SECRET }}
        run: |
          npx web-ext sign --no-input \
            --api-key="${FIREFOX_API_KEY}" \
            --api-secret="${FIREFOX_API_SECRET}" \
            --channel=unlisted \
            --source-dir="firefox-mv3" \
            --upload-source-code="${{ env.PACKAGE_NAME }}-${{ github.event.release.tag_name }}-sources.zip"

      - name: 'Upload to Release'
        uses: cssnr/upload-release-action@v1
        with:
          overwrite: true
          globs: web-ext-artifacts/*.xpi
          names: '${{ env.PACKAGE_NAME }}-firefox.xpi'

  update-mozilla:
    name: 'Update Mozilla'
    if: ${{ !github.event.release.prerelease }}
    runs-on: ubuntu-latest
    timeout-minutes: 5
    needs: [publish-mozilla]

    permissions:
      contents: write

    steps:
      - name: 'Checkout'
        uses: actions/checkout@v6
        with:
          persist-credentials: false

      - name: 'Mozilla Addon Update'
        uses: cssnr/mozilla-addon-update-action@v1
        with:
          url: 'https://github.com/${{ github.repository }}/releases/download/{version}/${{ env.PACKAGE_NAME }}-firefox.xpi'
          addon_id: ${{ env.MOZILLA_ID }}
          version: ${{ github.event.release.tag_name }}

      - name: 'Commit Action'
        id: commit
        uses: suzuki-shunsuke/commit-action@f12e2d628a4ab72dcefe7890ae07e8dbf1e201b9 # v0.1.1
        with:
          branch: master
          commit_message: 'Bump ${{ env.UPDATE_JSON }} to ${{ github.event.release.tag_name }}'
          #github_token: ${{ steps.app.outputs.token }}
          app_id: 146360
          app_private_key: ${{ secrets.APP_PRIVATE_KEY }}
          fail_on_self_push: false
```

For more examples, you can check out other projects using this action:  
https://github.com/cssnr/mozilla-addon-update-action/network/dependents

## Tags

The following rolling [tags](https://github.com/cssnr/mozilla-addon-update-action/tags) are maintained.

| Version&nbsp;Tag                                                                                                                                                                                                                       | Rolling | Bugs | Feat. |   Name    |  Target  | Example  |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-----: | :--: | :---: | :-------: | :------: | :------- |
| [![GitHub Tag Major](https://img.shields.io/github/v/tag/cssnr/mozilla-addon-update-action?sort=semver&filter=!v*.*&style=for-the-badge&label=%20&color=44cc10)](https://github.com/cssnr/mozilla-addon-update-action/releases/latest) |   ✅    |  ✅  |  ✅   | **Major** | `vN.x.x` | `vN`     |
| [![GitHub Tag Minor](https://img.shields.io/github/v/tag/cssnr/mozilla-addon-update-action?sort=semver&filter=!v*.*.*&style=for-the-badge&label=%20&color=blue)](https://github.com/cssnr/mozilla-addon-update-action/releases/latest) |   ✅    |  ✅  |  ❌   | **Minor** | `vN.N.x` | `vN.N`   |
| [![GitHub Release](https://img.shields.io/github/v/release/cssnr/mozilla-addon-update-action?style=for-the-badge&label=%20&color=red)](https://github.com/cssnr/mozilla-addon-update-action/releases/latest)                           |   ❌    |  ❌  |  ❌   | **Micro** | `vN.N.N` | `vN.N.N` |

You can view the release notes for each version on the [releases](https://github.com/cssnr/mozilla-addon-update-action/releases) page.

The **Major** tag is recommended. It is the most up-to-date and always backwards compatible.
Breaking changes would result in a **Major** version bump. At a minimum you should use a **Minor** tag.

# Support

If you run into any issues or need help getting started, please do one of the following:

- [Report an Issue](https://github.com/cssnr/mozilla-addon-update-action/issues)
- [Q&A Discussion](https://github.com/cssnr/mozilla-addon-update-action/discussions/categories/q-a)
- [Request a Feature](https://github.com/cssnr/mozilla-addon-update-action/issues/new?template=1-feature.yaml)
- [Chat with us on Discord](https://discord.gg/wXy6m2X8wY)

[![Features](https://img.shields.io/badge/features-brightgreen?style=for-the-badge&logo=rocket&logoColor=white)](https://github.com/cssnr/mozilla-addon-update-action/issues/new?template=1-feature.yaml)
[![Issues](https://img.shields.io/badge/issues-red?style=for-the-badge&logo=southwestairlines&logoColor=white)](https://github.com/cssnr/mozilla-addon-update-action/issues)
[![Discussions](https://img.shields.io/badge/discussions-blue?style=for-the-badge&logo=livechat&logoColor=white)](https://github.com/cssnr/mozilla-addon-update-action/discussions)
[![Discord](https://img.shields.io/badge/discord-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/wXy6m2X8wY)

# Contributing

If you would like to submit a PR, please review the [CONTRIBUTING.md](#contributing-ov-file).

Please consider making a donation to support the development of this project
and [additional](https://cssnr.com/) open source projects.

[![Ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/cssnr)

[![Actions Tools](https://raw.githubusercontent.com/smashedr/repo-images/refs/heads/master/actions/actions-tools.png)](https://actions-tools.cssnr.com/)

Additionally, you can support other [GitHub Actions](https://actions.cssnr.com/) I have published:

- [Stack Deploy Action](https://github.com/cssnr/stack-deploy-action?tab=readme-ov-file#readme)
- [Portainer Stack Deploy Action](https://github.com/cssnr/portainer-stack-deploy-action?tab=readme-ov-file#readme)
- [Docker Context Action](https://github.com/cssnr/docker-context-action?tab=readme-ov-file#readme)
- [Actions Up Action](https://github.com/cssnr/actions-up-action?tab=readme-ov-file#readme)
- [Webstore Publish Action](https://github.com/cssnr/webstore-publish-action?tab=readme-ov-file#readme)
- [Rhysd Actionlint Action](https://github.com/cssnr/actionlint-action?tab=readme-ov-file#readme)
- [Zensical Action](https://github.com/cssnr/zensical-action?tab=readme-ov-file#readme)
- [VirusTotal Action](https://github.com/cssnr/virustotal-action?tab=readme-ov-file#readme)
- [Homebrew Action](https://github.com/cssnr/homebrew-action?tab=readme-ov-file#readme)
- [Mirror Repository Action](https://github.com/cssnr/mirror-repository-action?tab=readme-ov-file#readme)
- [Update Version Tags Action](https://github.com/cssnr/update-version-tags-action?tab=readme-ov-file#readme)
- [Docker Tags Action](https://github.com/cssnr/docker-tags-action?tab=readme-ov-file#readme)
- [TOML Action](https://github.com/cssnr/toml-action?tab=readme-ov-file#readme)
- [Update JSON Value Action](https://github.com/cssnr/update-json-value-action?tab=readme-ov-file#readme)
- [JSON Key Value Check Action](https://github.com/cssnr/json-key-value-check-action?tab=readme-ov-file#readme)
- [Parse Issue Form Action](https://github.com/cssnr/parse-issue-form-action?tab=readme-ov-file#readme)
- [Cloudflare Purge Cache Action](https://github.com/cssnr/cloudflare-purge-cache-action?tab=readme-ov-file#readme)
- [Mozilla Addon Update Action](https://github.com/cssnr/mozilla-addon-update-action?tab=readme-ov-file#readme)
- [Package Changelog Action](https://github.com/cssnr/package-changelog-action?tab=readme-ov-file#readme)
- [NPM Outdated Check Action](https://github.com/cssnr/npm-outdated-action?tab=readme-ov-file#readme)
- [Label Creator Action](https://github.com/cssnr/label-creator-action?tab=readme-ov-file#readme)
- [Algolia Crawler Action](https://github.com/cssnr/algolia-crawler-action?tab=readme-ov-file#readme)
- [Create Pull Action](https://github.com/cssnr/create-pull-action?tab=readme-ov-file#readme)
- [Upload Release Action](https://github.com/cssnr/upload-release-action?tab=readme-ov-file#readme)
- [Check Build Action](https://github.com/cssnr/check-build-action?tab=readme-ov-file#readme)
- [Web Request Action](https://github.com/cssnr/web-request-action?tab=readme-ov-file#readme)
- [Get Commit Action](https://github.com/cssnr/get-commit-action?tab=readme-ov-file#readme)

<details><summary>❔ Unpublished Actions</summary>

These actions are not published on the Marketplace, but may be useful.

- [cssnr/create-files-action](https://github.com/cssnr/create-files-action?tab=readme-ov-file#readme) - Create various files from templates.
- [cssnr/draft-release-action](https://github.com/cssnr/draft-release-action?tab=readme-ov-file#readme) - Keep a draft release ready to publish.
- [cssnr/env-json-action](https://github.com/cssnr/env-json-action?tab=readme-ov-file#readme) - Convert env file to json or vice versa.
- [cssnr/push-artifacts-action](https://github.com/cssnr/push-artifacts-action?tab=readme-ov-file#readme) - Sync files to a remote host with rsync.
- [smashedr/update-release-notes-action](https://github.com/smashedr/update-release-notes-action?tab=readme-ov-file#readme) - Update release notes.
- [smashedr/combine-release-notes-action](https://github.com/smashedr/combine-release-notes-action?tab=readme-ov-file#readme) - Combine release notes.

---

</details>

<details><summary>📝 Template Actions</summary>

These are basic action templates that I use for creating new actions.

- [javascript-action](https://github.com/smashedr/javascript-action?tab=readme-ov-file#readme) - JavaScript
- [typescript-action](https://github.com/smashedr/typescript-action?tab=readme-ov-file#readme) - TypeScript
- [py-test-action](https://github.com/smashedr/py-test-action?tab=readme-ov-file#readme) - Dockerfile Python
- [test-action-uv](https://github.com/smashedr/test-action-uv?tab=readme-ov-file#readme) - Dockerfile Python UV
- [docker-test-action](https://github.com/smashedr/docker-test-action?tab=readme-ov-file#readme) - Docker Image Python

Note: The `docker-test-action` builds, runs and pushes images to [GitHub Container Registry](https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry).

---

</details>

For a full list of current projects visit: [https://cssnr.github.io/](https://cssnr.github.io/)

<a href="https://github.com/cssnr/mozilla-addon-update-action">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=cssnr/mozilla-addon-update-action&type=date&legend=bottom-right&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=cssnr/mozilla-addon-update-action&type=date&legend=bottom-right" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=cssnr/mozilla-addon-update-action&type=date&legend=bottom-right" />
 </picture>
</a>
