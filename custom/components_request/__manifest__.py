# -*- coding: utf-8 -*-
{
    'name': "Components Request",
    'version': '16.0.1.0.0',
    'author': "Cybrosys Technologies",
    'category': 'Sales',
    'summary': 'Components requests of employees',
    'description': """
     For creating components request from the employees
    """,
    'depends': ['base', 'mail', 'product', 'hr'],
    'data': ['security/component_request_security.xml',
             'security/ir.model.access.csv',
             'data/request_reference_sequence.xml',
             'views/component_request_view.xml',
             'views/components_view.xml'
             ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'AGPL-3',
}
