# -*- coding: utf-8 -*-
{
    'name': "POS Purchase Limit",
    'version': '16.0.1.0.0',
    'author': "Cybrosys_Technologies",
    'category': 'Sales/Point of Sale',
    'summary': 'Purchase limit for customers',
    'description': """
    Purchase limit for customers in pos
    """,
    'depends': ['base', 'point_of_sale', 'contacts'],
    'data': [
        'views/res_partner_view.xml',
    ],
    'assets': {
        'point_of_sale.assets': [
            'purchase_limit/static/src/js/**/*',
            'purchase_limit/static/src/xml/**/*',
           ],
     },
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'AGPL-3',
}
