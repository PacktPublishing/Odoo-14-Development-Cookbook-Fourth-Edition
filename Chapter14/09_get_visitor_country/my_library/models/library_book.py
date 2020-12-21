# -*- coding: utf-8 -*-
from odoo import models, fields


class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Library Book'
    _inherit = ['website.seo.metadata']


    name = fields.Char('Title', required=True)
    date_release = fields.Date('Release Date')
    author_ids = fields.Many2many('res.partner', string='Authors')
    image = fields.Binary(attachment=True)
    html_description = fields.Html()
    book_issue_ids = fields.One2many('book.issue', 'book_id')
    restrict_country_ids = fields.Many2many('res.country')


    def _default_website_meta(self):
        res = super(LibraryBook, self)._default_website_meta()
        res['default_opengraph']['og:image'] = self.env['website'].image_url(self, 'image')
        res['default_twitter']['twitter:image'] = self.env['website'].image_url(self, 'image')
        return res


class LibraryBookIssues(models.Model):
    _name = 'book.issue'

    book_id = fields.Many2one('library.book', required=True)
    submitted_by = fields.Many2one('res.users')
    issue_description = fields.Text()

