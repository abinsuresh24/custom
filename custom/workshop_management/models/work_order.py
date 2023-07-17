# -*- coding: utf-8 -*-
from datetime import datetime
from odoo.exceptions import MissingError
from odoo.tools.safe_eval import datetime
from odoo import api, fields, models, _


class WorkOrder(models.Model):
    """Class defined for creating work order"""
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
    start_date = fields.Datetime(string="Start date")
    end_date = fields.Datetime(string="End date")
    notes = fields.Html(string="Notes")
    extra_components_ids = fields.One2many('extra.components', 'extra_comp_id',
                                           string="Extra Components")
    mechanic_id = fields.Many2one('hr.employee', string="Mechanic")
    hourly_cost = fields.Monetary(related="mechanic_id.hourly_cost",
                                  currency_field='company_currency_id')
    company_id = fields.Many2one('res.company', string='Company', readonly=True,
                                 default=lambda self: self.env.company)
    company_currency_id = fields.Many2one('res.currency',
                                          related='company_id.currency_id',
                                          string="Company Currency",
                                          readonly=True)
    service_cost = fields.Float(string='Service cost')
    material_order_ids = fields.One2many('material.order', 'material_order_id',
                                         string="Material orders")
    invoice_id = fields.Many2one('account.move', string="Invoice")

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
        """Function defined for calculating the start time of the work"""
        if not self.mechanic_id:
            raise MissingError("Please select a Mechanic to start the work")
        self.start_date = fields.Datetime.now()
        self.write({'state': 'running'})

    def stop_work(self):
        """Function defined for calculating the end time of the work"""
        self.end_date = fields.Datetime.now()
        print(self.end_date)

    def request_approval(self):
        """Function defined for requesting approval from
        the customers to add extra components"""
        self.write({'state': 'hold'})
        print("req")

    def work_confirm(self):
        """Function defined for confirming the work order"""
        mail_template = self.env.ref(
            'workshop_management.work_done_email_template')
        mail_template.send_mail(self.id, force_send=True)
        self.write({'state': 'repaired'})

    def work_cancel(self):
        """Function defined for cancel the work order"""
        print("5")

    def create_invoice(self):
        """Function defined for creating invoice for the materials used
        in the work order and work cost of the mechanic"""
        self.invoice_id = self.env['account.move'].create(
            {'move_type': 'out_invoice',
             'partner_id': self.customer_id.id,
             'state': 'draft',
             'invoice_date': fields.Date.today(),
             })
        for rec in self.material_order_ids:
            self.env['account.move.line'].create({
                'product_id': rec.materials_id.id,
                'move_id': self.invoice_id.id,
                'quantity': rec.quantity,
                'price_unit': rec.price})
        return {
            'type': 'ir.actions.act_window',
            'name': 'Invoice',
            'res_model': 'account.move',
            'view_mode': 'form',
            'move_type': 'out_invoice',
            'res_id': self.invoice_id.id,
            'target': 'current'
        }

    @api.depends('start_date', 'end_date')
    def calculate_cost(self):
        """Function defined for calculating the work cost for the work order"""
        if self.start_date and self.end_date:
            start_date = datetime.strptime(str(self.start_date),
                                           '%Y-%m-%d %H:%M:%S')
            end_date = datetime.strptime(str(self.end_date),
                                         '%Y-%m-%d %H:%M:%S')
            self.service_cost = (end_date - start_date).total_seconds() / 3600
            print(self.service_cost)

    def smart_button_appointment(self):
        """Function defined for appointment smart button in the work order"""
        appointment = self.env['workshop.appointment'].search(
            [('appointment_no', '=', self.appointment_no)])
        return {
            'type': 'ir.actions.act_window',
            'name': 'appointment',
            'view_mode': 'form',
            'res_model': 'workshop.appointment',
            'domain': [('id', '=', appointment.id)],
            'context': {'create': False}
        }

    def create_report(self):
        """Function defined for creating report for the work order"""
        data = {'form_data': self.read()[0]}
        print(data)
        return self.env.ref(
            'workshop_management.action_report_work_order').report_action(
            self, data=data)
