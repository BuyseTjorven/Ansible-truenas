import json
import requests
r = requests.post(
  'ws://192.168.32.153/websocket',
  auth=('admin', 'tjorven'),
  headers={'Content-Type': 'application/json'},
  verify=False,
  data=json.dumps({
       'bsdusr_uid': '1100',
       'bsdusr_username': 'myuser',
       'bsdusr_mode': '755',
       'bsdusr_creategroup': 'True',
       'bsdusr_password': '12345',
       'bsdusr_shell': '/usr/local/bin/bash',
       'bsdusr_full_name': 'Full Name',
       'bsdusr_email': 'name@provider.com',
   })
 )
print(r.text)

