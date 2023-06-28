# -*- coding: utf-8 -*-
from odoo import fields, models


class CrmTeam(models.Model):
    """class defined for adding commission in the crm sale team"""
    _inherit = 'crm.team'

    commission_plan_id = fields.Many2one('crm.commission',
                                         string="Commission plan",
                                         help="Crm commission plans")
