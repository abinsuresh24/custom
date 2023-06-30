# -*- coding: utf-8 -*-
from odoo import fields, models


class ResUsers(models.Model):
    _inherit = 'res.partner'
    _description = "model for customer"

    purchase_limit = fields.Boolean(string="Purchase limit")
    purchase_amount = fields.Float(string="Purchase amount")
