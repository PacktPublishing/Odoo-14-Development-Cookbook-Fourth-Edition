# -*- coding: utf-8 -*-
from odoo import models, fields


class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Library Book'

    name = fields.Char('Title', required=True)
    date_release = fields.Date('Release Date',
        groups='my_library.group_release_dates')
    author_ids = fields.Many2many('res.partner', string='Authors')
    is_public = fields.Boolean(groups='my_library.group_library_librarian')
    private_notes = fields.Text(groups='my_library.group_library_librarian')

