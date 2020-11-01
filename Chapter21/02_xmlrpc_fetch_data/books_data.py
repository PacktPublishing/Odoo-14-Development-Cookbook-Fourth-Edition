from xmlrpc import client

server_url = 'http://localhost:8069'
db_name = 'book-db-14'
username = 'admin'
password = 'admin'

common = client.ServerProxy('%s/xmlrpc/2/common' % server_url)
user_id = common.authenticate(db_name, username, password, {})

models = client.ServerProxy('%s/xmlrpc/2/object' % server_url)

if user_id:
    search_domain = ['|', ['name', 'ilike', 'odoo'], ['name', 'ilike', 'sql']]
    books_ids = models.execute_kw(db_name, user_id, password,
        'library.book', 'search',
        [search_domain],
        {'limit': 5})
    print('Books ids found:', books_ids)

    books_data = models.execute_kw(db_name, user_id, password,
        'library.book', 'read',
        [books_ids, ['name', 'date_release']])
    print("Books data:", books_data)
else:
    print('Wrong credentials')