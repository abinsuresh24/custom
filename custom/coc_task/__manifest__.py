# -*- coding: utf-8 -*-
{
    'name': "Coc task",
    'version': '16.0.1.0.0',
    'author': "Cybrosys Technologies",
    'category': 'Sales',
    'summary': 'Coc',
    'description': """
     coc
    """,
    'depends': ['base', 'sale_management'],
    'data': [
             'views/sale_order_view.xml',
             'views/res_partner_view.xml',
             ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'AGPL-3',
}
