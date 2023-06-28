# -*- coding: utf-8 -*-
from odoo import fields, models


class ResUsers(models.Model):
    """class defined for adding commission in the salesperson"""
    _inherit = 'res.users'

    salesperson_commission_id = fields.Many2one('crm.commission',
                                                string="Commission plan",
                                                help="Crm commission plans")
