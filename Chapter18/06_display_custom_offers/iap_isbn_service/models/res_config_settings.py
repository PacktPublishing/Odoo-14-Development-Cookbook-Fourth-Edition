# -*- coding: utf-8 -*-
from odoo import models, fields


class ConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    isbn_service_key = fields.Char("ISBN service key", config_parameter='iap.isbn_service_key')
