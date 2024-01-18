import requests
import json

url = 'http://192.168.32.153/api/v2.0/auth/check_password'
headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer 1-MAKPeh2hHaWvyAO4gS3RME9R0cPJFzUOfU4uko6UcklUbNpKM9pqHZMNioGqxNwY'
}
data = {
    "username": "admin",
    "password": "tjorven"
}

response = requests.post(url, headers=headers, data=json.dumps(data))

print(response.text)