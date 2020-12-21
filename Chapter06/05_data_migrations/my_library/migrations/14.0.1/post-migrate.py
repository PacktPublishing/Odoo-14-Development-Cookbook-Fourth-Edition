# -*- coding: utf-8 -*-
from odoo import fields
from datetime import date

# NOTE: This is just for demo purpose
# This function invoked only if system already have 14.0.0 version installed

def migrate(cr, version):
    cr.execute('SELECT id, date_release_char FROM library_book')
    for record_id, old_date in cr.fetchall():
        # check if the field happens to be set in Odoo's internal
        # format
        new_date = None
        try:
            new_date = fields.Date.to_date(old_date)
        except ValueError:
            if len(old_date) == 4 and old_date.isdigit():
                # probably a year
                new_date = date(int(old_date), 1, 1)
            else:
                # try some separators, play with day/month/year
                # order ...
                pass
        if new_date:
            cr.execute('UPDATE library_book SET date_release=%s',
                       (new_date,))