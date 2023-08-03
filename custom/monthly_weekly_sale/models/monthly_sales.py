# -*- coding: utf-8 -*-
import base64

from odoo import api, fields, models
from odoo.exceptions import ValidationError


class MonthlySales(models.Model):
    """Class representing monthly sales and weekly sales"""
    _name = 'monthly.sales'
    _description = 'Monthly Sales'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'report_type'

    partner_ids = fields.Many2many('res.partner', string='Partner',
                                   required=True)
    sales_team_id = fields.Many2one('crm.team', string='Sales Team',
                                    required=True)
    date_from = fields.Date(string='Date From')
    date_to = fields.Date(string='Date To')
    report_type = fields.Selection(
        [('monthly', 'Monthly'), ('weekly', 'Weekly')])
    today = fields.Date.today()
    partner_name = fields.Char(string='Partner Name')

    @api.onchange('date_to')
    def onchange_date_to(self):
        """Function to check date is valid or not."""
        if self.date_from:
            if self.date_to < self.date_from:
                raise ValidationError(
                    "Date To should be greater than Date From")

    def send_pdf_report_monthly(self):
        """Function to send pdf report monthly"""
        line = self.search([])
        for line in line:
            if line.date_from and line.date_to:
                if line.report_type == 'monthly' and line.date_from < line.today and line.today < line.date_to:
                    query = """select s.name as order_no,s.create_date,p.name,
                            s.amount_total from sale_order as s inner join 
                            res_partner as p on p.id = s.partner_id where 1=1"""
                    if line.sales_team_id:
                        query += """ and s.team_id = '%s'""" % line.sales_team_id.id
                    self.env.cr.execute(query)
                    sale_data = self.env.cr.dictfetchall()
                    data = {'form_data': line.read()[0], 'sale_data': sale_data}
                    for rec in line.partner_ids:
                        line.partner_name = rec.name
                        sale_report = self.env.ref(
                            'monthly_weekly_sale.action_report_sale_order')
                        data_record = base64.b64encode(
                            self.env[
                                'ir.actions.report'].sudo()._render_qweb_pdf(
                                sale_report, [line.id], data=data)[0])
                        ir_values = {
                            'name': 'Sale order',
                            'type': 'binary',
                            'datas': data_record,
                            'store_fname': data_record,
                            'mimetype': 'application/pdf',
                            'res_model': 'monthly.sales',
                        }
                        sale_report_attachment_id = self.env[
                            'ir.attachment'].sudo().create(
                            ir_values)
                        if sale_report_attachment_id:
                            email_template = self.env.ref(
                                'monthly_weekly_sale.sale_report_email_template')
                            if rec.email:
                                email = rec.email
                            else:
                                email = 'admin@example.com'
                            if email_template and email:
                                email_values = {
                                    'email_to': email,
                                    'email_cc': False,
                                    'scheduled_date': False,
                                    'recipient_ids': [],
                                    'partner_ids': [],
                                    'auto_delete': True,
                                }
                                email_template.attachment_ids = [
                                    (4, sale_report_attachment_id.id)]
                                email_template.with_context(partner=rec,
                                                            inv=line).send_mail(
                                    line.id, email_values=email_values,
                                    force_send=True)
                                email_template.attachment_ids = [(5, 0, 0)]

    def send_pdf_report_weekly(self):
        """Function to send pdf report weekly"""
        line = self.search([])
        for line in line:
            if line.report_type == 'weekly' and line.date_from < line.today and line.today < line.date_to:
                query = """select s.name as order_no,s.create_date,p.name,
                        s.amount_total from sale_order as s inner join 
                        res_partner as p on p.id = s.partner_id where 1=1"""
                if line.sales_team_id:
                    query += """ and s.team_id = '%s'""" % line.sales_team_id.id
                self.env.cr.execute(query)
                sale_data = self.env.cr.dictfetchall()
                data = {'form_data': line.read()[0], 'sale_data': sale_data}
                for rec in line.partner_ids:
                    line.partner_name = rec.name
                    sale_report = self.env.ref(
                        'monthly_weekly_sale.action_report_sale_order')
                    data_record = base64.b64encode(
                        self.env['ir.actions.report'].sudo()._render_qweb_pdf(
                            sale_report, [line.id], data=data)[0])
                    ir_values = {
                        'name': 'Sale order',
                        'type': 'binary',
                        'datas': data_record,
                        'store_fname': data_record,
                        'mimetype': 'application/pdf',
                        'res_model': 'monthly.sales',
                    }
                    sale_report_attachment_id = self.env[
                        'ir.attachment'].sudo().create(
                        ir_values)
                    if sale_report_attachment_id:
                        email_template = self.env.ref(
                            'monthly_weekly_sale.sale_report_email_template')
                        if rec.email:
                            email = rec.email
                        else:
                            email = 'admin@example.com'
                        if email_template and email:
                            email_values = {
                                'email_to': email,
                                'email_cc': False,
                                'scheduled_date': False,
                                'recipient_ids': [],
                                'partner_ids': [],
                                'auto_delete': True,
                            }
                            email_template.attachment_ids = [
                                (4, sale_report_attachment_id.id)]
                            email_template.with_context(partner=rec,
                                                        inv=line).send_mail(
                                line.id, email_values=email_values,
                                force_send=True)
                            email_template.attachment_ids = [(5, 0, 0)]
