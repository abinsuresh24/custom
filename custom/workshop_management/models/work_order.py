# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class WorkOrder(models.Model):
    _name = 'work.order'
    _description = "Work order details"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = "order_no"

    order_no = fields.Char(string='Order', readonly=True,
                           default=lambda self: _('New'))
    appointment_no = fields.Char(string="Appointment no", readonly=True)
    customer_id = fields.Many2one('res.partner', string="Customer")
    vehicle_id = fields.Many2one('fleet.vehicle', string="Vehicle")
    booking_date = fields.Date(string="Booking date",
                               default=fields.Date.today())
    appointment_date = fields.Date(string="Appointment date")
    odo_meter = fields.Float(string="Odo-meter")
    phone = fields.Char(related='customer_id.phone', string="Phone")
    state = fields.Selection([('draft', 'Draft'), ('repaired', 'Repaired')],
                             string='State', default='draft')
    orderline_ids = fields.One2many('sale.order.line', 'work_order_id',
                                    string="Order lines")
    start_date = fields.Date(string="Start date")
    end_date = fields.Date(string="End date")

    @api.model
    def create(self, vals_list):
        """Declaring function for creating unique sequence number
        for each order"""
        if vals_list.get('order_no', 'New') == 'New':
            vals_list['order_no'] = self.env['ir.sequence'].next_by_code(
                'workshop.order.sequence') or 'New'
        result = super().create(vals_list)
        return result

    def work_confirm(self):
        print("4")

    def work_cancel(self):
        print("5")
