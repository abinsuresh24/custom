# -*- coding: utf-8 -*-
{
    'name': "Product Visibility",
    'version': '16.0.1.0.0',
    'author': "Cybrosys_Technologies",
    'category': 'Website',
    'summary': 'Product visibility for customers',
    'description': """
    Show only the allowed products in shop when the related user is logged in
    """,
    'depends': ['base', 'website', 'website_sale', 'contacts'],
    'data': [
        'views/res_partner_view.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'AGPL-3',
}
