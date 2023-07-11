# -*- coding: utf-8 -*-
from odoo import fields, models


class PaymentProvider(models.Model):
    _inherit = 'payment.provider'

    code = fields.Selection(selection_add=[('multisafepay', "Multisafepay")],
                            ondelete={'multisafepay': 'set default'})
    multisafepay_website_key = fields.Char(string="Website Key",
                                           help="The key solely used to identify"
                                                " the website with multisafepay",
                                           required_if_provider='paytm')
    multisafepay_secret_key = fields.Char(string="Multisafepay Secret Key",
                                          required_if_provider='multisafepay',
                                          groups='base.group_system')
