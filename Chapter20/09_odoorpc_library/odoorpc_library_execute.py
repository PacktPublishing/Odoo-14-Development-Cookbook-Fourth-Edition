import odoorpc

db_name = 'book-db-14'
user_name = 'admin'
password = 'admin'

# Prepare the connection to the server
odoo = odoorpc.ODOO('localhost', port=8069)
odoo.login(db_name, user_name, password)  # login

books_info = odoo.execute('library.book', 'search_read',
    [['name', 'ilike', 'odoo']], ['name', 'date_release'])
print(books_info)