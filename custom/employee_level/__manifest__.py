# -*- coding: utf-8 -*-
{
    'name': "Employee Level",
    'version': '16.0.1.0.0',
    'author': "Cybrosys Technologies",
    'category': 'Sales',
    'summary': 'Employee Level',
    'description': """
     Details about the employees level of the company
    """,
    'depends': ['base', 'hr'],
    'data': ['security/ir.model.access.csv',
             'views/employee_level_view.xml',
             'views/emp_level_view.xml',
             'views/hr_employee_view.xml',
             ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'AGPL-3',
}
