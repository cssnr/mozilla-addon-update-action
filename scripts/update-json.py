import json
import os
from typing import Any, Dict, Optional

print(os.environ)

input_url = os.environ['INPUT_URL']
input_manifest = os.environ['INPUT_MANIFEST']
input_update = os.environ['INPUT_UPDATE']
input_addon_id = os.environ['INPUT_ADDON_ID']


def add_version(url: str,
                manifest_file: str = 'manifest.json',
                update_file: str = 'update.json',
                addon_id: Optional[str] = None) -> Dict[str, Any]:

    with open(manifest_file) as f:
        manifest = json.load(f)
    with open(update_file) as f:
        update = json.load(f)
    addition = {
        'version': f"{manifest['version']}",
        'update_link': url.format(version=manifest['version']),
    }
    addon_id = addon_id or manifest['browser_specific_settings']['gecko']['id']
    update['addons'][addon_id]['updates'].append(addition)
    return update


result = add_version(input_url, input_manifest, input_update, input_addon_id)
data = json.dumps(result, indent=2)
print(data)

with open(input_update, 'w') as update_json:
    update_json.write(data + '\n')
