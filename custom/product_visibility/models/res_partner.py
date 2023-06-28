# -*- coding: utf-8 -*-
from odoo import fields, models


class ResPartner(models.Model):
    """Class defined for adding new field in the contacts module"""
    _inherit = 'res.partner'
    _description = 'Option to add allowed products in Customers'

    product_ids = fields.Many2many('product.template', string='Products',
                                   help="Only selected products "
                                        "will show in the website")
    product_category_ids = fields.Many2many('product.public.category',
                                            string="Product category",
                                            help="Only selected product category "
                                                 "will show in the website")
    product = fields.Boolean(string="Product")
