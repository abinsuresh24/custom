# -*- coding: utf-8 -*-
from odoo import api, fields, models


class ResPartner(models.Model):
    """Class defined for adding product code
    field in the model"""
    _inherit = 'res.partner'
    _description = "inherited sale order model"

    product_code = fields.Char(string="Product Code")