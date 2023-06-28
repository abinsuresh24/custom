# -*- coding: utf-8 -*-
from odoo import fields, models


class StockPicking(models.Model):
    """Class defined for adding a One-2-many field in the stock_picking model"""
    _inherit = 'stock.picking'
    _description = 'track order transfer details'

    track_order_ids = fields.One2many('track.order', 'order_id',
                                      string="Track order")
