# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
from odoo import api, fields, models, _


class WorkshopAppointment(models.Model):
    _name = 'workshop.appointment'
    _description = "Workshop appointment details"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = "appointment_no"

    appointment_no = fields.Char(string="Appointment number", readonly=True,
                                 default=lambda self: _('New'))
    customer_id = fields.Many2one('res.partner', string="Name",
                                  help="Name of the customer")
    address = fields.Char(related='customer_id.contact_address',
                          string="Address")
    phone = fields.Char(related='customer_id.phone', string="Phone")
    email = fields.Char(related='customer_id.email', string="Email")
    state = fields.Selection([('draft', 'Draft'), ('confirmed', 'Confirmed'),
                              ('cancelled', 'Cancelled')],
                             string='State', default='draft')
    vehicle_id = fields.Many2one('fleet.vehicle', string="Vehicle",
                                 help="Vehicle to repair")
    total_km = fields.Float(string="Total Kilometer",
                            help="Total odo-meter reading")
    booking_date = fields.Date(string="Booking date",
                               default=fields.Date.today())
    appointment_date = fields.Date(string='Appointment date',
                                   help="Appointment date for the service")
    compliant_ids = fields.One2many('workshop.complaints', 'workshop_id')
    responsible_id = fields.Many2one('res.users', 'Responsible User',
                                     default=lambda self: self.env.user)
    company_id = fields.Many2one('res.company', string="Company name",
                                 help="Company name",
                                 default=lambda self: self.env.company)
    description = fields.Char(string="Description", default=lambda self: _(
        'APPOINTMENT CONFIRMATION MAIL'))

    def appointment_confirm(self):
        # mail_template = self.env.ref(
        #     'workshop_management.confirmation_email_template')
        # mail_template.send_mail(self.id, force_send=True)
        self.write({'state': 'confirmed'})

    def appointment_cancel(self):
        self.write({'state': 'cancelled'})

    @api.model
    def create(self, vals_list):
        """Declaring function for creating unique sequence number
        for each booking"""
        if vals_list.get('appointment_no', 'New') == 'New':
            vals_list['appointment_no'] = self.env['ir.sequence'].next_by_code(
                'workshop.appointment.sequence') or 'New'
        result = super().create(vals_list)
        return result

    def reminder_mail(self):
        print("haii")
        #     mail_template = self.env.ref(
        #         'workshop_management.reminder_email_template')
        #     mail_template.send_mail(self.id, force_send=True)
