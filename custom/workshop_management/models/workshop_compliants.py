# -*- coding: utf-8 -*-
from odoo import fields, models


class WorshopAppointment(models.Model):
    _name = 'workshop.complaints'
    _description = "Workshop complaints details"

    complaints = fields.Char(string="Complaints",
                             help="Specify your vehicle complaints")
    workshop_id = fields.Many2one('workshop.appointment',invisible=1)
