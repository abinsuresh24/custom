# -*- coding: utf-8 -*-
from odoo import api, fields, models
from odoo.exceptions import ValidationError


class SurveySurvey(models.Model):
    """Class defined for adding contact relation in survey model"""
    _inherit = "survey.survey"
    _description = "Inherited survey model"

    contact_relation_ids = fields.One2many('contact.relation',
                                           'survey_relation_id',
                                           string="Contact Relation")
