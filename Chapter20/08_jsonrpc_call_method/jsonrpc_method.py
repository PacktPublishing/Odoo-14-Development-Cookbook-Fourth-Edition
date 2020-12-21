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
    # Create the book in draft state
    payload = get_json_payload("object", "execute_kw",
        db_name, user_id, password,
        'library.book', 'create', [{'name': 'Book 1', 'state': 'draft'}])
    res = requests.post(json_endpoint, data=payload, headers=headers).json()
    print("Book created with id:", res['result'])
    book_id = res['result']

    # Change the book state by calling make_available method
    payload = get_json_payload("object", "execute_kw",
        db_name, user_id, password,
        'library.book', 'make_available', [book_id])
    res = requests.post(json_endpoint, data=payload, headers=headers).json()

    # Check the book status after method call
    payload = get_json_payload("object", "execute_kw",
        db_name, user_id, password,
        'library.book', 'read', [book_id, ['name', 'state']])
    res = requests.post(json_endpoint, data=payload, headers=headers).json()
    print("Book state after the method call:", res['result'])

else:
    print("Failed: wrong credentials")
