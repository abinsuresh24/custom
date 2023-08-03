# -*- coding: utf-8 -*-
{
    'name': "Monthly Weekly Sales Report",
    'version': '16.0.1.0.0',
    'author': "Cybrosys Technologies",
    'category': 'Sales',
    'summary': 'Monthly Weekly Sales Report Application',
    'description': """
     Details about the monthly,weekly sales report
    """,
    'depends': ['base', 'sale_management'],
    'data': ['security/ir.model.access.csv',
             'data/schedule_mail.xml',
             'data/sale_report_mail.xml',
             'views/monthly_sales_view.xml',
             'views/monthly_sales_menu.xml',
             'reports/report.xml',
             'reports/sale_order_templates_report.xml',
             ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'AGPL-3',
}
