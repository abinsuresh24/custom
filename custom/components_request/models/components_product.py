"""Components product"""
# -*- coding: utf-8 -*-
from odoo import fields, models


class ComponentsProduct(models.Model):
    """Class defined for adding components to the component request model"""
    _name = 'components.product'
    _description = "component request details"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = "product_id"

    product_id = fields.Many2one('product.product', string="Components",
                                 required=True)
    price = fields.Float(string="Price")
    quantity = fields.Integer(string="Quantity", default=1)
    vendor_ids = fields.Many2many('res.partner', string="Vendors")
    request_option = fields.Selection([('purchase_order', 'Purchase Order'), (
        'internal_transfer', 'Internal Transfer')], string="Request option",
                                      required=True)
    component_id = fields.Many2one('components.request', string="Components")
