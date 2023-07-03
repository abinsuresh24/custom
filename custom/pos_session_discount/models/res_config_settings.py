# -*- coding: utf-8 -*-
from ast import literal_eval

from odoo import api, fields, models


class ConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    pos_categ_discount = fields.Boolean(string="Discounts for Categories",
                                        store=True,
                                        config_parameter='pos_session_discount.pos_categ_discount')
    pos_max_discount = fields.Float(string="Max Discount",
                                    config_parameter='pos_session_discount.pos_categ_discount')
    pos_categ_ids = fields.Many2many('pos.category', 'pos_categ_rel',
                                     string="Categories")

    def set_values(self):
        res = super(ConfigSettings, self).set_values()
        self.env['ir.config_parameter'].sudo().set_param(
            'pos_session_discount.pos_categ_ids', self.pos_categ_ids.ids)
        return res

    @api.model
    def get_values(self):
        res = super(ConfigSettings, self).get_values()
        with_user = self.env['ir.config_parameter'].sudo()
        category_ids = with_user.get_param(
            'pos_session_discount.pos_categ_ids')
        res.update(
            pos_categ_ids=[
                (6, 0, literal_eval(category_ids))] if category_ids else False)
        return res
