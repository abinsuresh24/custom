# -*- coding: utf-8 -*-
from odoo.http import request
from odoo.addons.survey.controllers.main import Survey


class SurveyForm(Survey):
    """Class defined creating contact form survey submission"""

    def survey_submit(self, survey_token, answer_token, **post):
        """Function defined for super the submit button"""
        val = super(SurveyForm, self).survey_submit(survey_token, answer_token,
                                                    **post)
        que = request.env['survey.question'].search(
            [('id', '=', post['question_id'])])
        contact = request.env['contact.relation'].search(
            [('question_id.title', '=', que.title)])
        field = contact.contact_details_id.name
        answer = post[post['question_id']]
        if answer:
            if field == 'name':
                request.env['res.partner'].create(
                    {field: answer, 'survey_contact': answer_token})
            else:
                request.env['res.partner'].search(
                    [('survey_contact', '=', answer_token)]).write(
                    {field: answer})
        return val
