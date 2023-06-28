# -*- coding: utf-8 -*-
from odoo import fields, models


class CrmCommission(models.Model):
    """Class defined for adding commission plans"""
    _name = 'crm.commission'
    _description = "crm commission plans"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'plan_name'

    plan_name = fields.Char(string="Commission plan")
    from_date = fields.Date(string="From date")
    plan_active = fields.Boolean(string="Active")
    to_date = fields.Date(string="To date")
    plan_type = fields.Selection(
        [('product_wise', 'Product wise'), ('revenue_wise', 'Revenue wise')],
        string="Plan type", required=True)
    revenue_type = fields.Selection(
        [('straight', 'Straight'), ('graduated', 'Graduated')])
    straight_rate = fields.Float(string="Rate", default=0,
                                 help="Commission rate on the basis of percentage")
    commission_product_ids = fields.One2many('commission.product',
                                             'products_wise_id',
                                             string="Product wise")
    commission_revenue_ids = fields.One2many('commission.revenue',
                                             'revenue_wise_id',
                                             string="Revenue wise")
