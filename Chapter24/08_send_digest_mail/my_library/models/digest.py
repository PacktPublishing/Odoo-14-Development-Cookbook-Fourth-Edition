# -*- coding: utf-8 -*-

from odoo import fields, models

class Digest(models.Model):
    _inherit = 'digest.digest'

    kpi_book_rent = fields.Boolean('Book Rent')
    kpi_book_rent_value = fields.Integer(compute='_compute_kpi_book_rent_value')

    def _compute_kpi_book_rent_value(self):
        for record in self:
            start, end, company = record._get_kpi_compute_parameters()
            record.kpi_book_rent_value = self.env['library.book.rent'].search_count([
                ('create_date', '>=', start),
                ('create_date', '<', end)
            ])
