# -*- coding: utf-8 -*-
from odoo import api, fields, models


class SaleOrder(models.Model):
    """Class defined for adding product owner
    field in the product_product model"""
    _inherit = 'sale.order'
    _description = "inherited sale order model"

    so = fields.Float(string="so")
    company_id = fields.Many2one('res.company', string='Company', readonly=True,
                                 default=lambda self: self.env.company)
    company_currency_id = fields.Many2one('res.currency',
                                          related='company_id.currency_id',
                                          string="Company Currency",
                                          readonly=True)

    @api.onchange('order_line')
    def onchange_order_line(self):
        for rec in self.order_line:
            if self.partner_id.product_code:
                self.order_line = [fields.Command.update(rec.id, {
                    'name': self.partner_id.product_code + rec.product_id.default_code})]
