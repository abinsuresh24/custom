# -*- coding: utf-8 -*-
from odoo import api, fields, models


class ContactRelation(models.Model):
    _name = 'contact.relation'
    _description = "contact relation for survey"

    survey_id = fields.Many2one('survey.survey')
    # def _question_ids_domain(self):
    #     return [('id', '=', self.survey_id.question_and_page_ids.ids)]

    question_id = fields.Many2one('survey.question', string="Questions")
    contact_details_id = fields.Many2one('ir.model.fields',
                                         string="Contact Details",
                                         domain="[('model_id', '=', 'res.partner'),('ttype','=','char')]")

    @api.onchange('question_id')
    def _onchange_que(self):
        domain = [('id', 'in', self.survey_id.question_and_page_ids.ids)]
        return {'domain': {'question_id': domain}}
