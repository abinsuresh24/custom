# -*- coding: utf-8 -*-
from odoo import fields, models


class ProductProduct(models.Model):
    """Class defined for adding discount tag
    field in the product_product model"""
    _inherit = 'product.product'
    _description = "inherited product.product model"

    discount_tag = fields.Char(string="Discount tag",
                               help="Discount tag used in the pos")
