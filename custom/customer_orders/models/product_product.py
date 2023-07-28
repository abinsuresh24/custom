# -*- coding: utf-8 -*-
from odoo import api, fields, models


class ProductProduct(models.Model):
    _inherit = 'product.product'
    _description = "Inherited product"

    # product_counts = fields.Char(string="Product order count")

    # def _count_of_products(self):
    #     self.product_counts = self.sale_count

    @api.onchange('lst_price')
    def _onchange_price(self):
        product = self.env['sale.order.line'].search(
            [('product_id.name', '=', self.name),
             ('order_id.state', '=', 'draft')])
        product.price_unit = self.lst_price
