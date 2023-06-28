# -*- coding: utf-8 -*-
from odoo import models


class ProductProduct(models.Model):
    """Class defined for adding a new button in product_product model"""
    _inherit = 'product.product'

    def purchase_order_confirmed(self):
        """Function defined for showing wizard on clicking the button"""
        return {
            'name': 'Purchase order',
            'type': 'ir.actions.act_window',
            'res_model': 'order.wizard',
            'view_mode': 'form',
            "target": 'new'
        }
