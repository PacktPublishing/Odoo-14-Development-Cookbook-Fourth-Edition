# -*- coding: utf-8 -*-
from odoo import models, fields, api


class BookInfo(models.Model):
    _name = 'book.info'

    name = fields.Char('Books Name', required=True)
    isbn = fields.Char('ISBN', required=True)
    date_release = fields.Date('Release Date')
    cover_image = fields.Binary('BooksCover')
    author_ids = fields.Many2many('res.partner', string='Authors')

    @api.model
    def _books_data_by_isbn(self, isbn):
        book = self.search([('isbn', '=', isbn)], limit=1)
        if book:
            return {
                'status': 'found',
                'data': {
                    'name': book.name,
                    'isbn': book.isbn,
                    'date_release': book.date_release,
                    'cover_image': book.cover_image,
                    'authors': [a.name for a in book.author_ids]
                }
            }
        else:
            return {
                'status': 'not found',
            }
