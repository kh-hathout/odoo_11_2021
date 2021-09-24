# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'MyEventsCloud.com - Events Twitter',
    'category': 'Website',
    'description': 'Add twitter scroller snippet in events',
    'summary': 'Add twitter scroller snippet in events',
    'support': 'support@MyEventsCloud.com',
    'website': 'https://MyEventsCloud.com',
    'version': '11.1',
    "author": "MyEventsCloud.com",
    "license": "AGPL-3",
    "installable": True,
    'description': """
Display tweets by event
========================

        """,
    'depends': ['website','event'],
    'data': [
        'security/ir.model.access.csv',
        'data/mec_twitter_data.xml',
        'views/mec_twitter_snippet_templates.xml'
    ],
    'installable': True,
}
