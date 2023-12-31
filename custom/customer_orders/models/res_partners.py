# -*- coding: utf-8 -*-
from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'
    _description = "Inherited res partner"

    customer_order_ids = fields.One2many('sale.order', 'partner_id',
                                         string="Customer orders")
    cust_order = fields.Boolean(string="Customer order")
    product_count = fields.Char(string="products", compute='_compute_count',
                                readonly=True)

    def _compute_count(self):
        for rec in self:
            rec.product_count = rec.env['product.product'].search_count(
                [(
                 'id', 'in', rec.customer_order_ids.order_line.product_id.ids)])

    def action_order_products(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'ordered_product',
            'view_mode': 'tree',
            'res_model': 'product.product',
            'domain': [('id', 'in',
                        self.customer_order_ids.order_line.product_id.ids)],
            'context': {'create': False}
        }
