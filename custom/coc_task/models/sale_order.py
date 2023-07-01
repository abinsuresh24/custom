# -*- coding: utf-8 -*-
from odoo import api, fields, models


class SaleOrderLine(models.Model):
    """Class defined for adding product owner
    field in the product_product model"""
    _inherit = 'sale.order.line'
    _description = "inherited sale.order model"

    sku = fields.Char(string="SKU")

    # @api.onchange('sku')
    # def search_product(self):
    #     if self.sku:
    #         product = self.env['product.product'].search([('sku', '=', self.sku)])
    #         print(product)
        # self.product_template_id=product
