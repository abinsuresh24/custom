# -*- coding: utf-8 -*-
{
    'name': "Website snippet",
    'version': '16.0.1.0.0',
    'author': "Cybrosys_Technologies",
    'category': 'Website',
    'summary': 'website snippet',
    'description': """
     snippets for website
    """,
    'depends': ['base', 'website'],
    'data': [
        'views/event_snippet_view.xml',
        'views/event_view.xml',
        'views/sale_order_view.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            '/website_snippet/static/src/js/event_snippet.js',
            '/website_snippet/static/src/xml/dynamic_snippet.xml',
        ],
    },
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'AGPL-3',
}
