# -*- coding: utf-8 -*-
from odoo import fields, models


class SaleOrder(models.Model):
    """Class defined for adding product owner
    field in the product_product model"""
    _inherit = 'sale.order'
    _description = "inherited sale model"

    so = fields.Float(string="so")
