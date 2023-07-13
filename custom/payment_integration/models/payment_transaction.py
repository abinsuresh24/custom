import requests
from odoo import models


class PaymentTransaction(models.Model):
    _inherit = 'payment.transaction'

    url = "https://testapi.multisafepay.com/v1/json/orders?api_key=a290dbc96af6224ea13040b4e30ca9867c063357"

    payload = {
        "payment_options": {"close_window": False},
        "customer": {
            "locale": "en_US",
            "disable_send_email": False
        },
        "checkout_options": {"validate_cart": False},
        "days_active": 30,
        "seconds_active": 2592000
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)

    print(response.text)
