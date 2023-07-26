# -*- coding: utf-8 -*-
{
    'name': "Contact creation from Survey",
    'version': '16.0.1.0.0',
    'author': "Cybrosys_Technologies",
    'category': 'Marketing/Surveys',
    'summary': 'Contact creation from survey',
    'description': """
     Contact creation from survey details""",
    'depends': ['base', 'survey'],
    'data': [
        'security/ir.model.access.csv',
        'views/survey_survey_view.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'AGPL-3',
}
