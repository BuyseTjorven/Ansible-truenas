import requests
from ansible.module_utils.basic import AnsibleModule

def check_if_deployed(module):
    api_url = f"http://{module.params['host']}/api/v2.0/chart/release"
    response = requests.get(api_url, headers={"Authorization": f"Bearer {module.params['api_key']}"})

    if response.status_code == 200:
        releases = response.json()
        for release in releases:
            if release['name'] == 'nextcloud-release':
                return True
    return False

def deploy_nextcloud(module):
    if check_if_deployed(module):
        module.exit_json(changed=False, msg=f"{module.params['release_name']} is already deployed, skipping.")
        return

    api_url = f"http://{module.params['host']}/api/v2.0/chart/release"

    nextcloud_config = {
        "catalog": "TRUENAS",
        "item": "nextcloud",
        "release_name": module.params['release_name'],
        "train": "charts",
        "version": "1.6.56",
        "values": {
            "dataVolume": {
                "datasetName": module.params['data_volume_path']
            },
            "databaseVolume": {
                "datasetName": module.params['db_volume_path']
            },
            "databaseBackupVolume": {
                "datasetName": module.params['db_backup_volume_path']
            },
            "extraMount": {
                "datasetName": module.params['extra_mount_path']
            }
        }
    }

    response = requests.post(api_url, headers={"Authorization": f"Bearer {module.params['api_key']}"}, json=nextcloud_config)

    if response.status_code in [200, 201]:
        module.exit_json(changed=True, msg="Nextcloud deployed successfully.")
    else:
        module.fail_json(msg="Failed to deploy Nextcloud: " + response.text)

def main():
    module_args = {
        'host': {'type': 'str', 'required': True},
        'api_key': {'type': 'str', 'required': True, 'no_log': True},
        'release_name': {'type': 'str', 'default': 'nextcloud'},
        'data_volume_path': {'type': 'str', 'required': True},
        'db_volume_path': {'type': 'str', 'required': True},
        'db_backup_volume_path': {'type': 'str', 'required': True},
        'extra_mount_path': {'type': 'str', 'required': True}
    }

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    deploy_nextcloud(module)

if __name__ == '__main__':
    main()