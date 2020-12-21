# -*- coding: utf-8 -*-
from odoo import fields, models


class ActWindowView(models.Model):
    _inherit = 'ir.actions.act_window.view'

    view_mode = fields.Selection(selection_add=[('m2m_group', 'M2m group')],
        ondelete={'m2m_group': 'cascade'})
