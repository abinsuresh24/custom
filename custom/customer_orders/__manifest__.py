# -*- coding: utf-8 -*-
{
    'name': "Customer Orders",
    'version': '16.0.1.0.0',
    'author': "Cybrosys Technologies",
    'category': 'Sales',
    'summary': 'Customer Orders',
    'description': """
     Details about the customers sale order details""",
    'depends': ['base', 'contacts','sale_management','product'],
    'data': ['security/ir.model.access.csv',
             'views/res_partner_view.xml',
             'views/product_product_view.xml',
             ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'AGPL-3',
}
