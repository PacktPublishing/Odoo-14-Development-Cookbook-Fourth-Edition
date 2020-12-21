# -*- coding: utf-8 -*-

# /!\/!\/!\/!\/!\/!\/!\/!\
# Note that this is just a sample code
# You need to add this file in __init__.py
# /!\/!\/!\/!\/!\/!\/!\/!\


from odoo import exceptions, models
from odoo.http import request


class IrHttp(models.AbstractModel):
    _inherit = 'ir.http'

    @classmethod
    def _auth_method_base_group_user(cls):
        cls._auth_method_user()
        if not request.env.user.has_group('base.group_user'):
            raise exceptions.AccessDenied()

    # this is for the exercise
    @classmethod
    def _auth_method_groups(cls, group_xmlids=None):
        cls._auth_method_user()
        if not any(map(request.env.user.has_group, group_xmlids or [])):
            raise exceptions.AccessDenied()


    # the controller will be like this add this in main.py

    @http.route('/my_module/all-books/group_user', type='http',
                auth='base_group_user')
    def all_books_mine_base_group_user(self):
        # your code
        return ...

    # this is for the exercise
    @http.route('/my_module/all-books/groups', type='http',
                auth='groups(base.group_no_one)')
    def all_books_mine_groups(self):
        # your code
        return ...