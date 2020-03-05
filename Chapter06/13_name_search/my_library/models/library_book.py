# -*- coding: utf-8 -*-
from odoo.exceptions import UserError
from odoo import models, fields, api


class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Library Book'

    name = fields.Char('Title', required=True)
    isbn = fields.Char('ISBN')
    date_release = fields.Date('Release Date')
    author_ids = fields.Many2many('res.partner', string='Authors')
    old_edition = fields.Many2one('library.book', string='Old Edition')

    def name_get(self):
        result = []
        for book in self:
            authors = book.author_ids.mapped('name')
            name = '%s (%s)' % (book.name, ', '.join(authors))
            result.append((book.id, name))
        return result

    @api.model
    def _name_search(self, name='', args=None, operator='ilike',
                     limit=100, name_get_uid=None):
        args = [] if args is None else args.copy()
        if not(name == '' and operator == 'ilike'):
            args += ['|', '|',
                ('name', operator, name),
                ('isbn', operator, name),
                ('author_ids.name', operator, name)
            ]
            books_ids = self.search(args).ids
            return self.browse(books_ids).name_get()
        return super(LibraryBook, self)._name_search(
            name=name, args=args, operator=operator,
            limit=limit, name_get_uid=name_get_uid)