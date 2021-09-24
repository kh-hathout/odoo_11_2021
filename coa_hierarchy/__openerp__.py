# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'COA hierarchy ',
    'version' : '1.0',
    'summary': 'hierarchy for the COA',
    'author' : "Aymen rahmani",
    'sequence': 30,
    'description': """ Chart of Accounts with hierarchy.
This module create parent and child relation in account""",
    'category' : 'Accounting & Finance',
    'depends' : ['account', 'account_accountant'],
    'data': [
        'views/account_account_view.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
