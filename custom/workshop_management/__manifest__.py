# -*- coding: utf-8 -*-
{
    'name': "Workshop Management",
    'version': '16.0.1.0.0',
    'author': "Cybrosys_Technologies",
    'category': 'Sales',
    'summary': 'Workshop Management Application',
    'description': """
     Details about workshop management and service details
    """,
    'depends': ['base', 'mail', 'account', 'contacts', 'fleet',
                'sale_management', 'hr', 'hr_timesheet'],
    'data': [
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'data/confirmation_mail.xml',
        'data/reminder_mail.xml',
        'data/reminder_scheduler.xml',
        'views/workshop_appointment_view.xml',
        'views/work_order_view.xml',
        'views/work_order_template.xml',
        'wizards/other_complaints_view.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'AGPL-3',
}
