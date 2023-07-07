# -*- coding: utf-8 -*-
{
    'name': "POS Discount Tag",
    'version': '16.0.1.0.0',
    'author': "Cybrosys_Technologies",
    'category': 'Sales/Point of Sale',
    'summary': 'Discount Tag for products',
    'description': """
    Show discount tag for the product in the pos reciepts
    """,
    'depends': ['base', 'point_of_sale', 'product'],
    'data': [
        'views/product_product_view.xml',
    ],
    'assets': {
        'point_of_sale.assets': [
            'discount_tag/static/src/css/**/*',
            'discount_tag/static/src/js/**/*',
            'discount_tag/static/src/xml/**/*',
           ],
     },
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'AGPL-3',
}
