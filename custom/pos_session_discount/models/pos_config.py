# -*- coding: utf-8 -*-
from odoo import fields, models


class PosConfig(models.Model):
    """Class defined for inheriting pos for adding discount limit in pos"""
    _inherit = 'pos.config'

    categ_discount = fields.Boolean(string="Discounts for Categories")
    max_discount = fields.Float(string="Max Discount")
    categ_ids = fields.Many2many('pos.category', 'pos_categ_rel',
                                 string="Categories")
