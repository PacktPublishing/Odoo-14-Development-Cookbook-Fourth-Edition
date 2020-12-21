from xmlrpc import client

server_url = 'http://localhost:8069'
db_name = 'book-db-14'
username = 'admin'
password = 'admin'

common = client.ServerProxy('%s/xmlrpc/2/common' % server_url)
user_id = common.authenticate(db_name, username, password, {})

models = client.ServerProxy('%s/xmlrpc/2/object' % server_url)

if user_id:
    # Create book with state draft
    book_id = models.execute_kw(db_name, user_id, password,
        'library.book', 'create',
        [{'name': 'New Book', 'date_release': '2019-01-26', 'state': 'draft'}])

    # Call make_available method on new book
    models.execute_kw(db_name, user_id, password,
        'library.book', 'make_available',
        [[book_id]])

    # check book status after method call
    book_data = models.execute_kw(db_name, user_id, password,
        'library.book', 'read',
        [[book_id], ['name', 'state']])
    print('Book state after method call:', book_data[0]['state'])
else:
    print('Wrong credentials')