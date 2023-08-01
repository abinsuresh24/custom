# -*- coding: utf-8 -*-
from odoo import api, fields, models


class OrderWizard(models.TransientModel):
    """Class defined for adding a wizard to the product model"""
    _name = 'order.wizard'
    _description = 'Purchase order wizard'

    quantity = fields.Integer(string="Quantity", default=1)
    price = fields.Float(string="Price")
    product_id = fields.Many2one('product.product', string="Product",
                                 domain="[('product_tmpl_id','=', active_id)]")
    vendor_id = fields.Many2one('res.partner', string="Vendor")
    model_name = fields.Char(string="Active")

    @api.model
    def default_get(self, fields):
        """Function for getting default value to the wizard"""
        active_model = self._context.get('active_model')
        if active_model == 'product.template':
            res = super().default_get(fields)
            active_id = self._context.get('active_id')
            product = self.env['product.template'].browse(active_id)
            if active_id:
                res['product_id'] = product.product_variant_id
                res['vendor_id'] = product.seller_ids.partner_id
                res['price'] = product.seller_ids.filtered(
                    lambda r: r.partner_id == product.seller_ids.partner_id[
                        0]).price
                res['model_name'] = active_model
            return res
        else:
            res = super().default_get(fields)
            active_id = self._context.get('active_id')
            product = self.env['product.product'].browse(active_id)
            if active_id:
                res['product_id'] = product.id
                res['vendor_id'] = product.product_tmpl_id.seller_ids.partner_id
                res['price'] = product.seller_ids.filtered(
                    lambda r: r.partner_id == product.seller_ids.partner_id[
                        0]).price
            return res

    def confirmed_order(self):
        """Function for creating RFQ with the product details"""
        if self.product_id.product_tmpl_id.seller_ids.partner_id:
            vendor = self.product_id.product_tmpl_id.seller_ids.partner_id[0]
        else:
            vendor = self.vendor_id
        value = {
            'order_line': [
                fields.Command.create(
                    {'product_id': self.product_id.id,
                     'product_qty': self.quantity,
                     'price_unit': self.price})]
        }
        purchase_order = self.env['purchase.order'].search(
            [('partner_id', '=', vendor.id), ('state', '=', 'draft')])
        if purchase_order:
            purchase_order.write(value)
            purchase_order.button_confirm()
        else:
            value['partner_id'] = self.vendor_id.id
            value['state'] = 'draft'
            purchase = self.env['purchase.order'].create(value)
            purchase.button_confirm()
