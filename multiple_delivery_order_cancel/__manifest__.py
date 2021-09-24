# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Cancel Multiple Delivery Orders',
    'version' : '1.0',
    'author':'Craftsync Technologies',
    'category': 'Stock',
    'maintainer': 'Craftsync Technologies',
    'description': "Enable mass cancel delivery order workflow.Even if delivery was transfered.Now user can select multi delivery order for cancel",
    'summary': "multi delivery order cancel by single click from list view",
    'website': 'https://www.craftsync.com/',
    'license': 'OPL-1',
    'support':'info@craftsync.com',
    'depends' : ['stock_picking_cancel_cs'],
    'data': [
	   'views/view_cancel_multi_picking.xml',
    ],    
    'installable': True,
    'application': True,
    'auto_install': False,
    'images': ['static/description/main_screen.png'],
    'price': 10.00,
    'currency': 'EUR',

}
