# -*- coding: utf-8 -*-
from odoo import models, fields, api
import re
from odoo.tools import email_split, email_escape_char


class LibraryBookRent(models.Model):
    _name = 'library.book.rent'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    book_id = fields.Many2one('library.book', 'Book', required=True)
    borrower_id = fields.Many2one('res.partner', 'Borrower', required=True)
    state = fields.Selection([('ongoing', 'Ongoing'), ('returned', 'Returned')],
                             'State', default='ongoing', required=True,
                             tracking=True)
    rent_date = fields.Date(default=fields.Date.today, tracking=True)
    return_date = fields.Date(tracking=True)

    @api.model
    def create(self, vals):
        book_rec = self.env['library.book'].browse(vals['book_id'])  # returns record set from for given id
        book_rec.make_borrowed()
        return super(LibraryBookRent, self).create(vals)

    def book_return(self):
        self.ensure_one()
        self.book_id.make_available()
        self.write({
            'state': 'returned',
            'return_date': fields.Date.today()
        })

    def book_return_reminder(self):
        template_id = self.env.ref('my_library.book_return_reminder')
        self.message_post_with_template(template_id.id)

    def book_return_reminder_qweb(self):
        self.message_post_with_view('my_library.book_return_reminder_qweb')

    @api.model
    def message_new(self, msg_dict, custom_values=None):
        self = self.with_context(default_user_id=False)
        if custom_values is None:
            custom_values = {}
        regex = re.compile("^\[(.*)\]")
        match = regex.match(msg_dict.get('subject')).group(1)
        book_id = self.env['library.book'].search([('name', '=', match), ('state', '=', 'available')], limit=1)
        custom_values['book_id'] = book_id.id
        email_from = email_escape_char(email_split(msg_dict.get('from'))[0])
        custom_values['borrower_id'] = self._search_on_partner(email_from)
        return super(LibraryBookRent, self).message_new(msg_dict, custom_values)
