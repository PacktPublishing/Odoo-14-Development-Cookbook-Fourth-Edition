# -*- coding: utf-8 -*-

import logging

from odoo import models
from odoo.tools import populate

_logger = logging.getLogger(__name__)

class BookData(models.Model):
    _inherit = 'library.book'
    _populate_sizes = {'small': 10, 'medium': 100, 'large': 500}

    def _populate_factories(self):

        return [
            ('name', populate.constant('Book no {counter}')),
        ]

