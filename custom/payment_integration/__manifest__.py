# -*- coding: utf-8 -*-
{
    'name': "MultiSafePay",
    'version': '16.0.1.0.0',
    'author': "Cybrosys_Technologies",
    'category': 'Accounting',
    'summary': 'Multisafepay integration',
    'description': """
    payment provider multisafepay integration
    """,
    'depends': ['base', 'payment'],
    'data': [
        'views/multisafe_payment.xml',
        'views/multisafepay_template.xml',
        'data/multisafepay_data.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'AGPL-3',
}