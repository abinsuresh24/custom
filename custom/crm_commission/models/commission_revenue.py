# -*- coding: utf-8 -*-
from odoo import fields, models


class CommissionRevenue(models.Model):
    """class defined for product wise commission model"""
    _name = 'commission.revenue'
    _description = "Revenue commission plans"

    sequence = fields.Integer(string="Sequence")
    from_amount = fields.Float(string="From Amount")
    to_amount = fields.Float(string="To Amount")
    rate = fields.Float(string="Rate")
    revenue_wise_id = fields.Many2one('crm.commission')
