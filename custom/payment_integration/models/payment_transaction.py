# -*- coding: utf-8 -*-
import logging
import pprint
import requests
import json

from werkzeug import urls

from odoo import _, models
from odoo.exceptions import ValidationError

from odoo.addons.payment_integration.controllers.main import \
    MultisafepayController

_logger = logging.getLogger(__name__)


class PaymentTransaction(models.Model):
    _inherit = 'payment.transaction'

    def _get_specific_rendering_values(self, processing_values):
        print(self.amount)
        print(processing_values['amount'])
        url = "https://testapi.multisafepay.com/v1/json/orders?api_key=2e84f7c246d3c37f6d12cc3e72b75065fa48be75"
        base_url = self.provider_id.get_base_url()
        redirect_url = urls.url_join(base_url,
                                     MultisafepayController._return_url)
        # webhook_url = urls.url_join(base_url,
        #                             MultisafepayController._webhook_url)
        payload = json.dumps({
            "type": "redirect",
            "order_id": self.reference,
            "gateway": "",
            "currency": self.currency_id.name,
            "amount": int(self.amount),
            "description": "Test order description",
            "payment_options": {
                "notification_url": "https://www.example.com/client/notification?type=notification",
                "notification_method": "POST",
                "redirect_url": f'{redirect_url}?ref={self.reference}',
                "cancel_url": "https://www.example.com/client/notification?type=cancel",
                "close_window": True
            },
            "customer": {
                "locale": 'en_US',
                "ip_address": "123.123.123.123",
                "first_name": self.partner_id.name,
                "last_name": self.partner_id.name,
                "company_name": "Test Company Name",
                "address1": "Kraanspoor",
                "house_number": "39C",
                "zip_code": "1033SC",
                "city": self.partner_id.street,
                "country": "NL",
                "phone": self.partner_id.phone,
                "email": self.partner_id.email,
                "referrer": "https://example.com",
                "user_agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36"
            }
        })
        print(payload, "payload")
        headers = {
            'Content-Type': 'application/json',
            'Cookie': 'PHPSESSID=l9b1a2nas4soml8soumke44n6b'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        print(response.text)
        response_json = response.text
        response_data = json.loads(response_json)
        print(response_data, "dataaa")
        payment_url = response_data["data"]["payment_url"]
        print(payment_url)
        res = super()._get_specific_rendering_values(processing_values)
        print("okkkkkkkkkkkk")
        if self.provider_code != 'multisafepay':
            return res

        # payload = self._multisafepay_prepare_payment_request_payload()
        _logger.info("sending '/orders' request for link creation:\n%s",
                     pprint.pformat(payload))
        payment_data = self.provider_id._multisafepay_make_request('/orders',
                                                                   data=payload)
        # print(payment_data)

        self.provider_reference = payment_data.get('id')
        parsed_url = urls.url_parse(payment_url)
        url_params = urls.url_decode(parsed_url.query)
        return {'api_url': payment_url, 'url_params': url_params}

    # def _multisafepay_prepare_payment_request_payload(self):
    #     # user_lang = self.env.context.get('lang')
    #     base_url = self.provider_id.get_base_url()
    #     redirect_url = urls.url_join(base_url,MultisafepayController._return_url)
    #     webhook_url = urls.url_join(base_url,
    #                                 MultisafepayController._webhook_url)
    #     return {
    #         'description': self.reference,
    #         'amount': {
    #             'currency': self.currency_id.name,
    #             'value': f"{self.amount:.2f}",
    #         },
    #         'locale': 'en_US',
    #         'redirectUrl': f'{redirect_url}?ref={self.reference}',
    #         'webhookUrl': f'{webhook_url}?ref={self.reference}',
    #     }

    def _get_tx_from_notification_data(self, provider_code, notification_data):
        print("notification", notification_data)
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
        url = "https://testapi.multisafepay.com/v1/json/orders/self.reference?api_key=2e84f7c246d3c37f6d12cc3e72b75065fa48be75"

        headers = {"accept": "application/json"}

        response = requests.get(url, headers=headers)

        print(response.text,"newwwwww")
        print(notification_data, "1212")
        super()._process_notification_data(notification_data)
        if self.provider_code != 'multisafepay':
            return

        payment_data = self.provider_id._multisafepay_make_request(
            f'/orders/{self.provider_reference}', method="GET")
        payment_status = payment_data.get('status')
        print(payment_data,"payment_data")
        print(payment_status,"payment_status")
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
                "received data with invalid payment status (%s) for transaction "
                "with reference %s", payment_status, self.reference
            )
            self._set_error(
                "Multisafepay: " + _(
                    "Received data with invalid payment status: %s",
                    payment_status)
            )
