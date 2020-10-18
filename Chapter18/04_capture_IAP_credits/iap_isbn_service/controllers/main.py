# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
from odoo.addons.iap.tools import iap_tools


class Main(http.Controller):
    @http.route('/get_book_data', type='json', auth="public")
    def get_book_data(self, account_token, isbn_number):
        service_key = request.env['ir.config_parameter'].sudo().get_param('iap.isbn_service_key', False)
        if not service_key:
            return {
                'status': 'service is not active'
            }
        credits_to_reserve = 1
        data = {}
        with iap_tools.iap_charge(request.env, service_key, account_token, credits_to_reserve):
            data = request.env['book.info'].sudo()._books_data_by_isbn(isbn_number)
            if data['status'] == 'not found':
                raise Exception('Book not found')
        return data