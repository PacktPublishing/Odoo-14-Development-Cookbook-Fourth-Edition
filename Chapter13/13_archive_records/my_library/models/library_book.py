# -*- coding: utf-8 -*-
from odoo import models, fields


class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Library Book'

    name = fields.Char('Title', required=True)
    date_release = fields.Date('Release Date')
    active = fields.Boolean(default=True)
    author_ids = fields.Many2many('res.partner', string='Authors')
    state = fields.Selection(
        [('available', 'Available'),
         ('borrowed', 'Borrowed'),
         ('lost', 'Lost')],
        'State', default="available")
    cost_price = fields.Float('Book Cost')
    category_id = fields.Many2one('library.book.category')

    rent_count = fields.Integer(compute="_compute_rent_count")

    def _compute_rent_count(self):
        BookRent = self.env['library.book.rent']
        for book in self:
            book.rent_count = BookRent.search_count([('book_id', '=', book.id)])

    def make_available(self):
        self.ensure_one()
        self.state = 'available'

    def make_borrowed(self):
        self.ensure_one()
        self.state = 'borrowed'

    def make_lost(self):
        self.ensure_one()
        self.state = 'lost'


