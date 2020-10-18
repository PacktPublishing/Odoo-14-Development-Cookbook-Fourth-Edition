# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import UserError
from odoo.addons.iap.tools import iap_tools


class LibraryBook(models.Model):
    _inherit = 'library.book'

    cover_image = fields.Binary('Books Cover')
    isbn = fields.Char('ISBN')

    def fetch_book_data(self):
        self.ensure_one()
        if not self.isbn:
            raise UserError("Please add  ISBN number")

        user_token = self.env['iap.account'].get('book_isbn')
        params = {
            'account_token': user_token.account_token,
            'isbn_number': self.isbn
        }
        service_endpoint = 'http://localhost:8070'
        result = iap_tools.iap_jsonrpc(service_endpoint + '/get_book_data', params=params)
        if result.get('status') == 'found':
            self.write(self.process_result(result['data']))
        return True

    @api.model
    def process_result(self, result):
        authors = []
        existing_author_ids = []
        for author_name in result['authors']:
            author = self.env['res.partner'].search([('name', '=', author_name)], limit=1)
            if author:
                existing_author_ids.append(author.id)
            else:
                authors.append((0, 0, {'name': author_name}))
        if existing_author_ids:
            authors.append((6, 0, existing_author_ids))
        return {
            'author_ids': authors,
            'name': result.get('name'),
            'isbn': result.get('isbn'),
            'cover_image': result.get('cover_image'),
            'date_release': result.get('date_release'),
        }