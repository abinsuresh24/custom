# -*- coding: utf-8 -*-
from odoo import fields, models


class ProductProduct(models.Model):
    """Class defined for adding product owner
    field in the product_product model"""
    _inherit = 'product.product'
    _description = "inherited product variant model"

    owner_id = fields.Many2one('res.partner', string="Product Owner")