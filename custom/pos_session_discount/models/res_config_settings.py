# -*- coding: utf-8 -*-
from odoo import fields, models


class ConfigSettings(models.TransientModel):
    """Class defined for inheriting pos for adding
    discount limit in pos settings"""
    _inherit = 'res.config.settings'

    pos_categ_discount = fields.Boolean(related='pos_config_id.categ_discount',
                                        readonly=False)
    pos_max_discount = fields.Float(related='pos_config_id.max_discount',
                                    readonly=False)
    pos_categ_ids = fields.Many2many('pos.category',
                                     related='pos_config_id.categ_ids',
                                     readonly=False)
