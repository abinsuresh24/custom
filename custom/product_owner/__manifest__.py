# -*- coding: utf-8 -*-
{
    'name': "Product Owner",
    'version': '16.0.1.0.0',
    'author': "Cybrosys_Technologies",
    'category': 'Sales/Point of Sale',
    'summary': 'Product owner for products',
    'description': """
    Show owner of the product in the pos reciepts
    """,
    'depends': ['base', 'point_of_sale', 'product'],
    'data': [
        'views/product_product_view.xml',
    ],
    'assets': {
        'point_of_sale.assets': [
            'product_owner/static/src/js/**/*',
            'product_owner/static/src/xml/**/*',
           ],
     },
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'AGPL-3',
}
