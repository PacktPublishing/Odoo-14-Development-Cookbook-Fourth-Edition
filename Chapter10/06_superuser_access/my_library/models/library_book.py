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
    report_missing = fields.Text(
        string="Book is missing",
        groups='my_library.group_library_librarian')

    def report_missing_book(self):
        self.ensure_one()
        message = "Book is missing (Reported by: %s)" % self.env.user.name
        self.sudo().write({
            'report_missing': message
        })


