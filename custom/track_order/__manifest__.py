# -*- coding: utf-8 -*-
{
    'name': "Track Order",
    'version': '16.0.1.0.0',
    'author': "Cybrosys_Technologies",
    'category': 'Website',
    'summary': 'Track order of transfers',
    'description': """
     Tracking the details of orders in transfers
    """,
    'depends': ['base', 'website', 'stock', 'portal'],
    'data': [
        'security/ir.model.access.csv',
        'views/stock_picking_view.xml',
        'views/track_order_template_view.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'AGPL-3',
}
