# -*- coding: utf-8 -*-
import datetime

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
    odo_meter = fields.Float(string="Total Odo-meter")
    phone = fields.Char(related='customer_id.phone', string="Phone")
    state = fields.Selection(
        [('draft', 'Draft'), ('running', 'Running'), ('hold', 'Hold'),
         ('repaired', 'Repaired')], string='State', default='draft')
    orderline_ids = fields.One2many('sale.order.line', 'work_order_id',
                                    string="Order lines")
    start_date = fields.Datetime(string="Start date")
    end_date = fields.Datetime(string="End date")
    notes = fields.Html(string="Notes")
    extra_components_ids = fields.One2many('extra.components', 'extra_comp_id',
                                           string="Extra Components")
    mechanic_id = fields.Many2one('hr.employee', string="Mechanic", required=True)
    hourly_cost = fields.Monetary(related="mechanic_id.hourly_cost",
                                  currency_field='company_currency_id')
    company_id = fields.Many2one('res.company', string='Company', readonly=True,
                                 default=lambda self: self.env.company)
    company_currency_id = fields.Many2one('res.currency',
                                          related='company_id.currency_id',
                                          string="Company Currency",
                                          readonly=True)
    service_cost = fields.Float(string='Service cost', compute="_compute_cost")
    material_order_ids = fields.One2many('material.order', 'material_order_id',
                                         string="Material orders")

    @api.model
    def create(self, vals_list):
        """Declaring function for creating unique sequence number
        for each order"""
        if vals_list.get('order_no', 'New') == 'New':
            vals_list['order_no'] = self.env['ir.sequence'].next_by_code(
                'workshop.order.sequence') or 'New'
        result = super().create(vals_list)
        return result

    def start_work(self):
        self.start_date = fields.Datetime.now()
        self.write({'state': 'running'})

    def stop_work(self):
        self.end_date = fields.Datetime.now()
        print(self.end_date)

    def request_approval(self):
        self.write({'state': 'hold'})
        print("req")

    def work_confirm(self):
        self.write({'state': 'repaired'})
        print("4")

    def work_cancel(self):
        print("5")

    def create_invoice(self):
        invoice = self.env['account.move'].create(
            {'move_type': 'out_invoice',
             'partner_id': self.customer_id.id,
             'state': 'draft',
             'invoice_date': fields.Date.today(),
             'invoice_line_ids': [
                 fields.Command.create(
                     {'product_id': self.orderline_ids.product_template_id.id,
                      'quantity': self.orderline_ids.product_uom_qty,
                      'price_unit': self.orderline_ids.price_unit})]
             })
        return {
            'type': 'ir.actions.act_window',
            'name': 'Invoice',
            'res_model': 'account.move',
            'view_mode': 'form',
            'move_type': 'out_invoice',
            'res_id': invoice.id,
            'target': 'current'
        }

    @api.depends('start_date', 'end_date')
    def calculate_duration_hours(self):
        if self.start_date and self.end_date:
            start_date = datetime.strptime(str(self.start_date),
                                           '%Y-%m-%d %H:%M:%S')
            end_date = datetime.strptime(str(self.end_date),
                                         '%Y-%m-%d %H:%M:%S')
            self.service_cost = (end_date - start_date).total_seconds() / 3600
            print(self.service_cost)
