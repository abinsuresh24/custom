# -*- coding: utf-8 -*-
from odoo import api, fields, models


class ProductProduct(models.Model):
    """Class defined for adding product owner
    field in the product_product model"""
    _inherit = 'product.product'
    _description = "inherited product.product model"

    sku = fields.Char(string="SKU")

    @api.model
    def _name_search(self, name='', args=None, operator='ilike', limit=100, name_get_uid=None):
        args = list(args or [])
        if name:
            args += ['|', '|', ('sku', '=', name),]
        return self._search(args, limit=limit, access_rights_uid=name_get_uid)