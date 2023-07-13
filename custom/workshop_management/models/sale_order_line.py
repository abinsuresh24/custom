# -*- coding: utf-8 -*-
from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order.line'
    _description = "Inherited sale order line"

    work_order_id = fields.Many2one('work.order',string='Work order')
