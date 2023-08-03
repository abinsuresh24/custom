# -*- coding: utf-8 -*-
from odoo import api, fields, models


class ProductTemplate(models.Model):
    """Class defined for adding product owner
    field in the product_product model"""
    _inherit = 'product.template'
    _description = "inherited product.product model"


