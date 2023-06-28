# -*- coding: utf-8 -*-
{
    'name': "Automated Purchase Order",
    'version': '16.0.1.0.0',
    'author': "Cybrosys Technologies",
    'category': 'Sales',
    'summary': 'Automated Purchase Order extras',
    'description': """
     For creating purchase order from product form
    """,
    'depends': ['base', 'product'],
    'data': ['security/ir.model.access.csv',
             'views/product_template_view.xml',
             'views/product_product_view.xml',
             'wizards/product_purchase_order_view.xml',
             ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'AGPL-3',
}

