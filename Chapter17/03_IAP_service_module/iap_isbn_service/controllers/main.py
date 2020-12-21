# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class Main(http.Controller):
    @http.route('/get_book_data', type='json', auth="public")
    def get_book_data(self):
        # We will capture credit here
        return {
            'test': 'data'
        }