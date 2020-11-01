import json
import random
import requests


server_url = 'http://localhost:8069'
db_name = 'book-db-14'
username = 'admin'
password = 'admin'

json_endpoint = "%s/jsonrpc" % server_url
headers = {"Content-Type": "application/json"}


def get_json_payload(service, method, *args, **kwargs):
    kwargs = kwargs or {}
    return json.dumps({
        "jsonrpc": "2.0",
        "method": 'call',
        "params": {
            "service": service,
            "method": method,
            "args": args
        },
        "id": random.randint(0, 1000000000),
    })

payload = get_json_payload("common", "login", db_name, username, password)
response = requests.post(json_endpoint, data=payload, headers=headers)
user_id = response.json()['result']

if user_id:
    payload = get_json_payload("object", "execute_kw",
        db_name, user_id, password,
        'library.book', 'check_access_rights', ['create'])
    res = requests.post(json_endpoint, data=payload, headers=headers).json()
    print("Has create access:", res['result'])

else:
    print("Failed: wrong credentials")
