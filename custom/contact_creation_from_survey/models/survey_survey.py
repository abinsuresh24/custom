# -*- coding: utf-8 -*-
from odoo import api, fields, models


class SurveySurvey(models.Model):
    _inherit = "survey.survey"
    _description = "Inherited survey model"

    contact_relation_ids = fields.One2many('contact.relation', 'survey_id',
                                           string="Contact Relation")

    @api.onchange('contact_relation_ids')
    def _onchange_contact_relation_ids(self):
        question = self.env['survey.question'].search([])
        # for rec in self.contact_relation_ids:
        #     question=self.env['survey.question'].search([])
        #     print(question,"11")
