# -*- coding: utf-8 -*-
from odoo import fields, models


class SalesCommission(models.Model):
    """Class defined for adding new menu in the sale order"""
    _name = 'sales.commission'

    partner_id = fields.Many2one('res.partner', string="Partner")
    commission_amount = fields.Char(string="Commission amount")
    commission_plan_id = fields.Many2one('crm.commission',
                                         string="Commission_plan")
    reference_id = fields.Many2one('sale.order', string="Reference number")
