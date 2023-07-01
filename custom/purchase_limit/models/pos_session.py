# -*- coding: utf-8 -*-
from odoo import models


class PosSessions(models.Model):
    """Class defined for inheriting pos for adding product owner in pos"""
    _inherit = 'pos.session'

    def _loader_params_res_partner(self):
        """Function defined for appending product owner """
        result = super()._loader_params_res_partner()
        result['search_params']['fields'].append('purchase_amount')
        result['search_params']['fields'].append('purchase_limit')
        return result
