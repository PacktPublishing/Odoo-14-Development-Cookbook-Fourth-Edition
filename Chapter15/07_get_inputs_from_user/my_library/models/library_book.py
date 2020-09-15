# -*- coding: utf-8 -*-
from odoo import models, fields


class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Library Book'

    name = fields.Char('Title', required=True)
    date_release = fields.Date('Release Date')
    author_ids = fields.Many2many('res.partner', string='Authors')
    image = fields.Binary(attachment=True)
    html_description = fields.Html()
    book_issue_ids = fields.One2many('book.issue', 'book_id')


class LibraryBookIssues(models.Model):
    _name = 'book.issue'

    book_id = fields.Many2one('library.book', required=True)
    submitted_by = fields.Many2one('res.users')
    issue_description = fields.Text()

