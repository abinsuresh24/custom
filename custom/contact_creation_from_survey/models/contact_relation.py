# -*- coding: utf-8 -*-
from odoo import api, fields, models


class ContactRelation(models.Model):
    """Class defined for adding contact relation in survey model"""
    _name = 'contact.relation'
    _description = "contact relation for survey"

    survey_relation_id = fields.Many2one('survey.survey')

    question_id = fields.Many2one('survey.question', string="Questions")
    contact_details_id = fields.Many2one('ir.model.fields',
                                         string="Contact Details",
                                         domain="[('model_id', '=',"
                                                " 'res.partner'),"
                                                "('ttype','=','char')]")

    @api.onchange('question_id')
    def _onchange_que(self):
        """Function defined for setting domain for question in one2many field"""
        domain = [
            ('id', 'in', self.survey_relation_id.question_and_page_ids.ids)]
        return {'domain': {'question_id': domain}}
