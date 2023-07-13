# -*- coding: utf-8 -*-
from datetime import timedelta
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
                              ('to_work', 'To Work'),
                              ('cancelled', 'Cancelled')],
                             string='State', default='draft')
    vehicle_id = fields.Many2one('fleet.vehicle', string="Vehicle",
                                 domain="[('driver_id', '=', customer_id)]",
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

    def appointment_confirm(self):
        mail_template = self.env.ref(
            'workshop_management.confirmation_email_template')
        mail_template.send_mail(self.id, force_send=True)
        self.env['work.order'].create({
            'customer_id': self.customer_id.id,
            'appointment_no': self.appointment_no,
            'vehicle_id': self.vehicle_id.id,
            'appointment_date': self.appointment_date,
            'odo_meter': self.total_km,
        })
        self.write({'state': 'confirmed'})

    def appointment_cancel(self):
        self.write({'state': 'cancelled'})

    def vehicle_pickup(self):
        return {
            'name': 'Other complaints',
            'type': 'ir.actions.act_window',
            'res_model': 'other.complaints',
            'view_mode': 'form',
            "target": 'new',
            "context": {
                'active_id': self.id,
                'default_appointment': self.appointment_no,
            },
        }

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
        today = fields.Date.today()
        tomorrow = today + timedelta(days=1)
        print(today)
        print(tomorrow)
        for rec in self.search([]):
            if rec.appointment_date == tomorrow:
                print("yes")
                mail_template = self.env.ref(
                    'workshop_management.reminder_email_template')
                mail_template.send_mail(rec.id, force_send=True)
