# -*- coding: utf-8 -*-
from odoo import fields, models


class CommissionProduct(models.Model):
    """class defined for product wise commission model"""
    _name = 'commission.product'
    _description = "product commission plans"

    product_category_id = fields.Many2one('product.category',
                                          string="Product category")
    product_id = fields.Many2one('product.template', string="Products")
    rate = fields.Float(string="Rate")
    max_commission = fields.Float("Max Commission",
                                  help="Maximum commission amount")
    products_wise_id = fields.Many2one('crm.commission')
