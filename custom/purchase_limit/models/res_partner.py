# -*- coding: utf-8 -*-
from odoo import fields, models


class ResPartners(models.Model):
    """Class defined for inheriting res partner for
    adding purchase limit for customers"""
    _inherit = 'res.partner'
    _description = "model for customer"

    purchase_limit = fields.Boolean(string="Purchase limit",
                                    help="Enable the field for"
                                         " setting purchase limit")
    purchase_amount = fields.Float(string="Purchase amount",
                                   help="Total amount for the customer "
                                        "can purchase")
