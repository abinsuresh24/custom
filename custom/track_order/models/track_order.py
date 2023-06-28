# -*- coding: utf-8 -*-
from odoo import fields, models


class TrackOrder(models.Model):
    """CLass defined for adding fields in the model,which is used in the
    stock_picking model as a one-to-many field"""
    _name = 'track.order'
    _description = "Order details"

    from_location_id = fields.Many2one(related='order_id.location_id', string='From Location')
    to_loc_id = fields.Many2one('stock.location', string='To Location')
    order_id = fields.Many2one('stock.picking', string="Order details")
