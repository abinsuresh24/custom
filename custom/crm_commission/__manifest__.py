# -*- coding: utf-8 -*-
{
    'name': "Crm Commission",
    'version': '16.0.1.0.0',
    'author': "Cybrosys_Technologies",
    'category': 'sales',
    'summary': 'Crm commission plans',
    'description': """
     Details of crm commission plan
    """,
    'depends': ['base', 'mail', 'crm','sale_management'],
    'data': [
        'security/ir.model.access.csv',
        'views/crm_commission_view.xml',
        'views/crm_team_view.xml',
        'views/res_users_view.xml',
        'views/sale_order_view.xml',
        'views/sales_commission_view.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'AGPL-3',
}
