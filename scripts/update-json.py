import json
import os
from typing import Any, Dict

input_url = os.environ.get('INPUT_URL')
input_update = os.environ.get('INPUT_UPDATE')
input_manifest = os.environ.get('INPUT_MANIFEST')
input_version = os.environ.get('INPUT_VERSION')
input_addon_id = os.environ.get('INPUT_ADDON_ID')


def add_version(url: str,
                update_file: str,
                version: str,
                addon_id: str) -> Dict[str, Any]:
    addition = {
        'version': f"{version}",
        'update_link': url.format(version=version),
    }
    with open(update_file) as f:
        update = json.load(f)
    update['addons'][addon_id]['updates'].append(addition)
    return update


if not input_manifest and not (input_version or input_addon_id):
    raise ValueError('You must provide manifest or both version and addon_id')

if not os.path.isfile(input_update):
    raise ValueError('Unable to locate input_update:', input_update)

print(f'Using Update JSON: {input_update}')

if os.path.isfile(input_manifest):
    print(f'Reading Manifest: {input_manifest}')
    with open(input_manifest) as f:
        manifest = json.load(f)

version = input_version or manifest['version']
print(f'Addon Version: {version}')
addon_id = input_addon_id or manifest['browser_specific_settings']['gecko']['id']
print(f'Addon ID: {addon_id}')

result = add_version(input_url, input_update, version, addon_id)
data = json.dumps(result, indent=2)
print(data)

with open(input_update, 'w') as update_json:
    update_json.write(data + '\n')
