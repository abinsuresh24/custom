# -*- coding: utf-8 -*-
from odoo import api,fields, models


class MaterialOrder(models.Model):
    _name = 'material.order'
    _description = "material order details"

    materials = fields.Char(string="Materials")
    quantity = fields.Float(string="Quantity")
    price = fields.Float(string="Unit price")
    total_price = fields.Float(string="Total")
    material_order_id = fields.Many2one('work.order')

    @api.onchange('quantity','price')
    def total_amount(self):
        self.total_price =self.quantity * self.price
