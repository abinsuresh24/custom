# -*- coding: utf-8 -*-
from odoo import models


class ProductTemplate(models.Model):
    """Class defined for adding new button to the inherited
    product.template model"""
    _inherit = 'product.template'

    def purchase_order_confirm(self):
        """Function defined for showing wizard on clicking the button"""
        return {
            'name': 'Purchase order',
            'type': 'ir.actions.act_window',
            'res_model': 'order.wizard',
            'view_mode': 'form',
            "target": 'new'
        }
