# -*- coding: utf-8 -*-
from odoo import fields, models


class ResPartner(models.Model):
    """Class defined for adding new field in partner form"""
    _inherit = "res.partner"
    _description = "Inherited contacts model"

    survey_contact = fields.Char(string="Contact name")
