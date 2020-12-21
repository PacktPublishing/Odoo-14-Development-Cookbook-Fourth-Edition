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
    # search for the books ids
    search_domain = ['|', ['name', 'ilike', 'odoo'], ['name', 'ilike', 'sql']]
    payload = get_json_payload("object", "execute_kw",
        db_name, user_id, password,
        'library.book', 'search', [search_domain], {'limit': 5})
    res = requests.post(json_endpoint, data=payload, headers=headers).json()
    print('Search Result:', res)  # ids will be in result keys

    # read data for books ids
    payload = get_json_payload("object", "execute_kw",
        db_name, user_id, password,
        'library.book', 'read', [res['result'], ['name', 'date_release']])
    res = requests.post(json_endpoint, data=payload, headers=headers).json()
    print('Books data:', res)
else:
    print("Failed: wrong credentials")
