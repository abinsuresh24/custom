# -*- coding: utf-8 -*-
import logging
import pprint

from odoo import http
from odoo.exceptions import ValidationError
from odoo.http import request

_logger = logging.getLogger(__name__)


class MultisafepayController(http.Controller):
    _return_url = '/payment/mollie/return'
    _webhook_url = '/payment/mollie/webhook'

    @http.route(
        _return_url, type='http', auth='public', methods=['GET', 'POST'], csrf=False,
        save_session=False
    )
    def mollie_return_from_checkout(self, **data):
        _logger.info("handling redirection from Mollie with data:\n%s", pprint.pformat(data))
        request.env['payment.transaction'].sudo()._handle_notification_data('mollie', data)
        return request.redirect('/payment/status')

    @http.route(_webhook_url, type='http', auth='public', methods=['POST'], csrf=False)
    def mollie_webhook(self, **data):
        _logger.info("notification received from Mollie with data:\n%s", pprint.pformat(data))
        try:
            request.env['payment.transaction'].sudo()._handle_notification_data('mollie', data)
        except ValidationError:  # Acknowledge the notification to avoid getting spammed
            _logger.exception("unable to handle the notification data; skipping to acknowledge")
        return ''  # Acknowledge the notification
