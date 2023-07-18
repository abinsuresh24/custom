# Part of Odoo. See LICENSE file for full copyright and licensing details.

import logging
import pprint

from werkzeug import urls

from odoo import _, models
from odoo.exceptions import ValidationError

from odoo.addons.payment_mollie.const import SUPPORTED_LOCALES
from odoo.custom.payment_integration.controllers.main import MultisafepayController


_logger = logging.getLogger(__name__)


class PaymentTransaction(models.Model):
    _inherit = 'payment.transaction'

    def _get_specific_rendering_values(self, processing_values):
        res = super()._get_specific_rendering_values(processing_values)
        if self.provider_code != 'multisafepay':
            return res

        payload = self._mollie_prepare_payment_request_payload()
        _logger.info("sending '/payments' request for link creation:\n%s", pprint.pformat(payload))
        payment_data = self.provider_id._multisafepay_make_request('/payments', data=payload)

        self.provider_reference = payment_data.get('id')
        checkout_url = payment_data['_links']['checkout']['href']
        parsed_url = urls.url_parse(checkout_url)
        url_params = urls.url_decode(parsed_url.query)
        return {'api_url': checkout_url, 'url_params': url_params}

    def _multisafepay_prepare_payment_request_payload(self):
        user_lang = self.env.context.get('lang')
        base_url = self.provider_id.get_base_url()
        redirect_url = urls.url_join(base_url, MultisafepayController._return_url)
        webhook_url = urls.url_join(base_url, MultisafepayController._webhook_url)

        return {
            'description': self.reference,
            'amount': {
                'currency': self.currency_id.name,
                'value': f"{self.amount:.2f}",
            },
            'locale': user_lang if user_lang in SUPPORTED_LOCALES else 'en_US',

            # Since Mollie does not provide the transaction reference when returning from
            # redirection, we include it in the redirect URL to be able to match the transaction.
            'redirectUrl': f'{redirect_url}?ref={self.reference}',
            'webhookUrl': f'{webhook_url}?ref={self.reference}',
        }

    def _get_tx_from_notification_data(self, provider_code, notification_data):
        tx = super()._get_tx_from_notification_data(provider_code, notification_data)
        if provider_code != 'multisafepay' or len(tx) == 1:
            return tx

        tx = self.search(
            [('reference', '=', notification_data.get('ref')), ('provider_code', '=', 'multisafepay')]
        )
        if not tx:
            raise ValidationError("Multisafepay: " + _(
                "No transaction found matching reference %s.", notification_data.get('ref')
            ))
        return tx

    def _process_notification_data(self, notification_data):
        super()._process_notification_data(notification_data)
        if self.provider_code != 'multisafepay':
            return

        payment_data = self.provider_id._multisafepay_make_request(
            f'/payments/{self.provider_reference}', method="GET"
        )
        payment_status = payment_data.get('status')

        if payment_status == 'pending':
            self._set_pending()
        elif payment_status == 'authorized':
            self._set_authorized()
        elif payment_status == 'paid':
            self._set_done()
        elif payment_status in ['expired', 'canceled', 'failed']:
            self._set_canceled("Multisafepay: " + _("Canceled payment with status: %s", payment_status))
        else:
            _logger.info(
                "received data with invalid payment status (%s) for transaction with reference %s",
                payment_status, self.reference
            )
            self._set_error(
                "Multisafepay: " + _("Received data with invalid payment status: %s", payment_status)
            )









# import requests
# from odoo import models
#
#
# class PaymentTransaction(models.Model):
#     _inherit = 'payment.transaction'
#
#     url = "https://testapi.multisafepay.com/v1/json/orders?api_key=a290dbc96af6224ea13040b4e30ca9867c063357"
#
#     payload = {
#         "payment_options": {"close_window": False},
#         "customer": {
#             "locale": "en_US",
#             "disable_send_email": False
#         },
#         "checkout_options": {"validate_cart": False},
#         "days_active": 30,
#         "seconds_active": 2592000
#     }
#     headers = {
#         "accept": "application/json",
#         "content-type": "application/json"
#     }
#
#     response = requests.post(url, json=payload, headers=headers)
#
#     print(response.text)
