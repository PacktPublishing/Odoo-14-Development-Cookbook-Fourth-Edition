from xmlrpc import client

# books data with search_read method
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
        'library.book', 'search_read',
        [search_domain, ['name', 'date_release']],
        {'limit': 5})
    print('Books data:', books_ids)

else:
    print('Wrong credentials')