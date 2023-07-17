# -*- coding: utf-8 -*-
from odoo import fields, models


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