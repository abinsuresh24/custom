# -*- coding: utf-8 -*-
{
    'name': "POS Session Wise Discount",
    'version': '16.0.1.0.0',
    'author': "Cybrosys_Technologies",
    'category': 'Sales/Point of Sale',
    'summary': 'POS Session Wise Discount',
    'description': """
    POS Session Wise Discount for categories in pos
    """,
    'depends': ['base', 'point_of_sale'],
    'data': [
        'views/res_config_settings_view.xml',
    ],
    'assets': {
        'point_of_sale.assets': [
            'pos_session_discount/static/src/js/**/*',
           ],
     },
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'AGPL-3',
}
