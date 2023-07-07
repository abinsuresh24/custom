# -*- coding: utf-8 -*-
from odoo import models


class PosSessions(models.Model):
    """Class defined for inheriting pos for adding discount category in pos"""
    _inherit = 'pos.session'

    def _pos_ui_models_to_load(self):
        result = super()._pos_ui_models_to_load()
        result.append('discount.category')
        return result

    def _loader_params_discount_category(self):
        return {
            'search_params': {
                'fields': ['category_id', 'pos_discount', 'pos_config_id'],
            },
        }

    def _get_pos_ui_discount_category(self, params):
        return self.env['discount.category'].search_read(**params['search_params'])
