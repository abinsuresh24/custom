# -*- coding: utf-8 -*-
from odoo import fields, models


class PosConfig(models.Model):
    """Class defined for inheriting pos for adding discount limit in pos"""
    _inherit = 'pos.config'

    categ_discount = fields.Boolean(string="Discounts for Categories",
                                    help="Category Discount")
    max_discount = fields.Float(string="Max Discount",
                                help="Maximum discount for products")
    categ_ids = fields.Many2many('pos.category', 'pos_categ_rel',
                                 string="Categories",
                                 help="Categories for appling discount limit")
    disc_category_ids = fields.One2many('discount.category',
                                        'discount_categ_id',
                                        string="Discount Category")
