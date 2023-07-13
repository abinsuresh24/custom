# -*- coding: utf-8 -*-
from odoo import fields, models


class OtherComplaints(models.TransientModel):
    """Class defined for creating wizard for report"""
    _name = 'other.complaints'
    _description = 'Other complaints wizard'

    other_complaints = fields.Char(string="Other complaints")
    appointment = fields.Char(string='Appointment')

    def confirm_complaints(self):
        active_id = self.env.context.get('active_id')
        active_model = self.env.context.get('active_model')
        print(active_model)
        if self.other_complaints:
            self.env['workshop.complaints'].search(
                [('workshop_id', '=', self.appointment)]).write(
                {active_model: [fields.Command.link(self.other_complaints)]})
        self.env['workshop.appointment'].search([('id', '=', active_id)]).write(
            {'state': 'to_work'})
