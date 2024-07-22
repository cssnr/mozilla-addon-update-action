import json
import os

input_url = os.environ.get('INPUT_URL')
input_update = os.environ.get('INPUT_UPDATE')
input_manifest = os.environ.get('INPUT_MANIFEST')
input_version = os.environ.get('INPUT_VERSION')
input_addon_id = os.environ.get('INPUT_ADDON_ID')

if not input_manifest and not (input_version or input_addon_id):
    raise ValueError('You must provide a manifest or both version and addon_id')

if not os.path.isfile(input_update):
    raise ValueError('Unable to locate update file:', input_update)

print(f'Using update file: {input_update}')

if os.path.isfile(input_manifest):
    print(f'Reading manifest: {input_manifest}')
    with open(input_manifest) as f:
        manifest = json.load(f)

version = input_version or manifest['version']
print(f'Addon version: {version}')
addon_id = input_addon_id or manifest['browser_specific_settings']['gecko']['id']
print(f'Addon ID: {addon_id}')
url = input_url.format(version=version)
print(f'Update URL: {url}')

with open(input_update) as f:
    result = json.load(f)

addition = {
    'version': version,
    'update_link': url,
}

result['addons'][addon_id]['updates'].append(addition)

data = json.dumps(result, indent=2)
print(data)

with open(input_update, 'w') as update_json:
    update_json.write(data + '\n')

with open(os.environ['GITHUB_OUTPUT'], 'a') as f:
    print(f'url={url}', file=f)
    print(f'result={json.dumps(result)}', file=f)

print('Finished Success.')
