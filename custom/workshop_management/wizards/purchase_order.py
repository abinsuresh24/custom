# -*- coding: utf-8 -*-
from odoo import fields, models
from odoo.exceptions import MissingError


class PurchaseOrder(models.TransientModel):
    """Class defined for creating wizard for adding additional notes"""
    _name = 'work.purchase'
    _description = 'Purchase Order wizard'

    product_id = fields.Many2one('product.product', string="Product",
                                 required=True)
    vendor_id = fields.Many2one('res.partner', string='Vendor', required=True)
    quantity = fields.Float(string="Quantity", required=True)
    order_details = fields.Char(string="Order no")

    def confirm_order(self):
        """Function defined for creating purchase order for materials"""
        if self.product_id.qty_available > self.quantity:
            raise MissingError("THE PRODUCT IS AVAILABLE IN THE STOCK")
        else:
            self.env['purchase.order'].create({"partner_id": self.vendor_id.id,
                                               'origin': self.order_details,
                                               'order_line': [
                                                   fields.Command.create(
                                                       {
                                                           'product_id': self.product_id.id,
                                                           'product_qty': self.quantity,
                                                       })]})
            self.env['work.order'].search(
                [('id', '=', self.order_details)]).write({'state': 'waiting'})