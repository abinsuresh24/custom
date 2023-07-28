# -*- coding: utf-8 -*-
from odoo import fields, models


class CustomerOrder(models.Model):
    _name = 'customer.order'
    _description = "Customer order details"

    cus_order_id = fields.Many2one('res.partner')
    order_details = fields.Char(string="Order details")
