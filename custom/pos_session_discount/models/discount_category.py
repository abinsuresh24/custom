# -*- coding: utf-8 -*-
from odoo import fields, models


class DiscountCategory(models.Model):
    """Class defined for adding one2many field in pos config model"""
    _name = 'discount.category'
    _description = "Discount limit for category"

    category_id = fields.Many2one('pos.category', string="Category")
    pos_discount = fields.Float(string="Discount")
    pos_config_id = fields.Many2one('pos.config', string="Pos config")
