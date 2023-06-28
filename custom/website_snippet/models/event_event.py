# -*- coding: utf-8 -*-
from odoo import fields, models


class EventEvent(models.Model):
    """Class defined for adding image field in the event_event model"""
    _inherit = 'event.event'

    image = fields.Image(string="Event image")
