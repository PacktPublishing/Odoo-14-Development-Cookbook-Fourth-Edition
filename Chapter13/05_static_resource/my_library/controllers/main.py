# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class Main(http.Controller):
    @http.route('/demo_page', type='http', auth='none')
    def books(self):
        image_url = '/my_library/static/src/image/odoo.png'
        html_result = """<html>
            <body>
                <img src="%s"/>
            </body>
        </html>""" % image_url
        return html_result
