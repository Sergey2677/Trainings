# -*- coding: utf-8 -*-
import random

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class SaleOrder(models.Model):
    _inherit = 'sale.order'


    test = fields.Char(store=True, default='', readonly=True, states={'draft': [('readonly', False)], 'sent': [('readonly', False)]})
    # Auxiliary field for capture the first two onchange triggers
    flag = fields.Integer(store=False)

    @api.onchange("date_order", "tax_totals_json", "flag")
    def _chain_date_and_total_with_test(self):
        for record in self:
            if int(record.flag) > 2 or '-' in record.test:
                record.test = f"{record.amount_total} - {record.date_order}"
            else:
                record.flag += 1
                record.test = random.randint(1, 100)

    # Method for checking value of test field
    @api.constrains('test')
    def _check_value(self):
        if self.test:
            if len(self.test) > 50:
                raise ValidationError("Длина текста должна быть меньше 50 символов!")