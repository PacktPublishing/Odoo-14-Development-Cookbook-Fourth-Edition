# -*- coding: utf-8 -*-
from odoo import http
from odoo.addons.website.controllers.main import Website


class WebsiteInfo(Website):
    @http.route()
    def website_info(self):
        result = super(WebsiteInfo, self).website_info()
        result.qcontext['apps'] = result.qcontext['apps'].filtered(
            lambda x: x.name != 'website'
        )
        return result