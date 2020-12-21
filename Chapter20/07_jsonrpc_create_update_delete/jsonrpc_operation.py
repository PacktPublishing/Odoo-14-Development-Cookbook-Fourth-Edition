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
    # creates the books records
    create_data = [
        {'name': 'Book 1', 'date_release': '2019-01-26'},
        {'name': 'Book 3', 'date_release': '2019-02-12'},
        {'name': 'Book 5', 'date_release': '2019-05-08'},
        {'name': 'Book 7', 'date_release': '2019-05-14'}
    ]
    payload = get_json_payload("object", "execute_kw", db_name, user_id, password, 'library.book', 'create', [create_data])
    res = requests.post(json_endpoint, data=payload, headers=headers).json()
    print("Books created:", res)
    books_ids = res['result']

    # Write in existing book record
    book_to_write = books_ids[1]  # We will use ids of recently created books
    write_data = {'name': 'Book 2'}
    payload = get_json_payload("object", "execute_kw", db_name, user_id, password, 'library.book', 'write', [book_to_write, write_data])
    res = requests.post(json_endpoint, data=payload, headers=headers).json()
    print("Books written:", res)

    # Delete in existing book record
    book_to_unlink = books_ids[2:]  # We will use ids of recently created books
    payload = get_json_payload("object", "execute_kw", db_name, user_id, password, 'library.book', 'unlink', [book_to_unlink])
    res = requests.post(json_endpoint, data=payload, headers=headers).json()
    print("Books deleted:", res)

else:
    print("Failed: wrong credentials")
