"""Components request"""
# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class ComponentsRequest(models.Model):
    """Class defined for creating component request for the employees"""
    _name = 'components.request'
    _description = "component request details"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = "partner_id"
    _order = 'reference desc'

    reference = fields.Char(string="Request reference", readonly=True,
                            default=lambda self: _('New'))
    partner_id = fields.Many2one('hr.employee', string="Employee name",
                                 required=True, help="Name of the employee")
    job_title = fields.Char(related='partner_id.job_title',
                            string='Job title')
    phone = fields.Char(related='partner_id.work_phone', string="Phone",
                        help="Phone number")
    email = fields.Char(related='partner_id.work_email', string="Email",
                        help='Email address')
    quotation_date = fields.Date(string="Quotation date",
                                 default=fields.Date.today())
    state = fields.Selection(
        [('draft', 'Draft'), ('first_approval', 'First Approval'),
         ('second_approval', 'Second Approval'), ('confirmed', 'Confirmed'),
         ('rejected', 'Rejected')],
        string='State', default='draft')
    components_ids = fields.One2many('components.product', 'component_id',
                                     string="Components")

    @api.model
    def create(self, vals_list):
        """Declaring function for creating unique sequence number
        for each booking"""
        if vals_list.get('reference', 'New') == 'New':
            vals_list['reference'] = self.env['ir.sequence'].next_by_code(
                'request.reference.sequence') or 'New'
        result = super().create(vals_list)
        return result

    def button_submit(self):
        """Function declared for creating component request by the employees"""
        self.write({'state': 'first_approval'})

    def first_approval_request(self):
        """Function declared for change the state to
        second approval on button click"""
        self.write({'state': 'second_approval'})

    def reject_approval_request(self):
        """Function declared for change the state to
               rejected on button click"""
        self.write({'state': 'rejected'})

    def second_approval_request(self):
        """Function declared for change the state to
               confirmed on button click"""
        for record in self.components_ids:
            if record.request_option == 'purchase_order':
                for rec in record.vendor_ids:
                    purchase = self.env['purchase.order'].create(
                        {
                            'partner_id': rec.id,
                            'state': 'draft',
                            'origin': self.id,
                            'order_line': [
                                fields.Command.create(
                                    {
                                        'product_id': record.id,
                                        'product_qty': record.quantity,
                                        'price_unit': record.price})]
                        })
                    purchase.button_confirm()
        self.write({'state': 'confirmed'})

    def request_reset_to_draft(self):
        """Function declared for change the state to
        second approval on button click"""
        self.write({'state': 'draft'})
