# Part of Odoo. See LICENSE file for full copyright and licensing details.

import logging
import pprint

from werkzeug import urls

from odoo import _, models
from odoo.exceptions import ValidationError

from odoo.addons.payment_integration.controllers.main import MultisafepayController

_logger = logging.getLogger(__name__)


class PaymentTransaction(models.Model):
    _inherit = 'payment.transaction'

    def _get_specific_rendering_values(self, processing_values):
        res = super()._get_specific_rendering_values(processing_values)
        print("okkkkkkkkkkkk")
        if self.provider_code != 'multisafepay':
            return res

        payload = self._multisafepay_prepare_payment_request_payload()
        _logger.info("sending '/orders' request for link creation:\n%s",
                     pprint.pformat(payload))
        payment_data = self.provider_id._multisafepay_make_request('/orders',
                                                                   data=payload)
        print(payment_data)

        self.provider_reference = payment_data.get('id')
        checkout_url = payment_data['data']['payment_url']
        parsed_url = urls.url_parse(checkout_url)
        url_params = urls.url_decode(parsed_url.query)
        return {'api_url': checkout_url, 'url_params': url_params}

    def _multisafepay_prepare_payment_request_payload(self):
        # user_lang = self.env.context.get('lang')
        base_url = self.provider_id.get_base_url()
        redirect_url = urls.url_join(base_url,
                                     MultisafepayController._return_url)
        webhook_url = urls.url_join(base_url,
                                    MultisafepayController._webhook_url)

        return {
            "type": "redirect",
            "order_id": "my-order-id-1",
            "gateway": "",
            "currency": "EUR",
            "amount": self.amount,
            "description": self.reference,
            "payment_options": {
                "notification_url": "https://www.example.com/client/notification?type=notification",
                "notification_method": "POST",
                "redirect_url": "https://www.example.com/client/notification?type=redirect",
                "cancel_url": "https://www.example.com/client/notification?type=cancel",
                "close_window": True
            },
            "customer": {
                "locale": "nl_NL",
                "ip_address": "123.123.123.123",
                "first_name": "John",
                "last_name": "Doe",
                "company_name": "Test Company Name",
                "address1": "Kraanspoor",
                "house_number": "39C",
                "zip_code": "1033SC",
                "city": "Amsterdam",
                "country": "NL",
                "phone": "0208500500",
                "email": "jdoe@example.com",
                "referrer": "https://example.com",
                "user_agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36"
            }
        }

    def _get_tx_from_notification_data(self, provider_code, notification_data):
        tx = super()._get_tx_from_notification_data(provider_code,
                                                    notification_data)
        if provider_code != 'multisafepay' or len(tx) == 1:
            return tx

        tx = self.search(
            [('reference', '=', notification_data.get('ref')),
             ('provider_code', '=', 'multisafepay')]
        )
        if not tx:
            raise ValidationError("Multisafepay: " + _(
                "No transaction found matching reference %s.",
                notification_data.get('ref')
            ))
        return tx

    def _process_notification_data(self, notification_data):
        super()._process_notification_data(notification_data)
        if self.provider_code != 'multisafepay':
            return

        payment_data = self.provider_id._multisafepay_make_request(
            f'/orders/{self.provider_reference}', method="GET"
        )
        payment_status = payment_data.get('status')

        if payment_status == 'pending':
            self._set_pending()
        elif payment_status == 'authorized':
            self._set_authorized()
        elif payment_status == 'paid':
            self._set_done()
        elif payment_status in ['expired', 'canceled', 'failed']:
            self._set_canceled(
                "Multisafepay: " + _("Canceled payment with status: %s",
                                     payment_status))
        else:
            _logger.info(
                "received data with invalid payment status (%s) for transaction with reference %s",
                payment_status, self.reference
            )
            self._set_error(
                "Multisafepay: " + _(
                    "Received data with invalid payment status: %s",
                    payment_status)
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
