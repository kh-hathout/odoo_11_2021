# -*- coding: utf-8 -*-
# Copyright 2020 CorTex IT Solutions Ltd. (<https://cortexsolutions.net/>)
# License OPL-1

{
    'name': "Multi Sale Orders Confirm",

    'summary': """
        This module enable you to confirm multi sale orders".
        """,
    'description': """
Multiple Sale Order Confirm
Multiple Sale Orders Confirm
Multiple SO Confirm
Multiple Confirm
Multi Sale Order Confirm
sale order confirm
confirm sale order
confirm multi sale order
so confirm 
sale confirm
sale multi confirm
sales multi confirm
sale order
so
sales multi confirm
Multi Sale Orders Confirm
Multi Sales Confirm
confirm multi sale orders
confirm multi SO's
confirm SO
multi confirm
    """,

    'author': 'CorTex IT Solutions Ltd.',
    'website': 'https://cortexsolutions.net',
    'license': 'OPL-1',
    'currency': 'EUR',
    'price': 10,
    'support': 'support@cortexsolutions.net',

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Sales',
    'version': '11.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['sale'],
    # always loaded
    'data': [
        'wizard/multi_so_confirm.xml',
    ],
    'images': ['static/description/main_screenshot.png'],
    "installable": True
}
