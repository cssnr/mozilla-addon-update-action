import json
import os
from typing import Any, Dict, Optional

input_url = os.environ.get('INPUT_URL')
input_update = os.environ.get('INPUT_UPDATE')
input_manifest = os.environ.get('INPUT_MANIFEST')
input_version = os.environ.get('INPUT_VERSION')
input_addon_id = os.environ.get('INPUT_ADDON_ID')


def add_version(url: str,
                manifest_file: str = 'manifest.json',
                update_file: str = 'update.json',
                version: Optional[str] = None,
                addon_id: Optional[str] = None) -> Dict[str, Any]:
    if manifest_file:
        with open(manifest_file) as f:
            manifest = json.load(f)
    _id = addon_id or manifest['browser_specific_settings']['gecko']['id']
    print(f'Addon ID: {_id}')
    ver = version or manifest['version']
    print(f'Addon Version: {ver}')
    addition = {
        'version': f"{ver}",
        'update_link': url.format(version=ver),
    }
    with open(update_file) as f:
        update = json.load(f)
    update['addons'][_id]['updates'].append(addition)
    return update


if not input_manifest and not (input_version or input_addon_id):
    raise ValueError('You must provide manifest or both version and addon_id')

result = add_version(input_url, input_manifest, input_update, input_version, input_addon_id)
data = json.dumps(result, indent=2)
print(data)

with open(input_update, 'w') as update_json:
    update_json.write(data + '\n')
