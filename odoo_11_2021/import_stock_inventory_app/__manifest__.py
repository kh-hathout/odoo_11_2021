# -*- coding: utf-8 -*-


{
    "name" : "Import Stock Inventory(Add/Update)",
    "author": "Edge Technologies",
    'version': '11.0.1.0',
    'live_test_url': "https://youtu.be/pCHq3VHv7ds",
    "images":['static/description/main_screenshot.png'],
    'summary': " Import Stock Inventory",
    'description': """ This app provides a functionality to import inventory adjustment from many given options .
import stock import inventory import import stocks import stock inventory adjustment import inventory adjustment
Stock Inventory import Import Stock Inventory Adjustment from CSV/Excel file Import Stock Inventory With Lot/Serial Number from CSV/Excel file Stock Inventory Adjustments Import Using CSV Import Delivery Orders Incoming Shipments and Internal Tranfer
Import Stock Inventory Adjustment From CSV/Xlsx Import Stock Inventory with Serial/Lot Number Import Stock Inventory by CSV/Xlsx Import Stock Inventory by Barcode
 import Delivery Orders  import Incoming Shipments import Internal Transfer Import Picking
 import multiple pickings import warehosue data Import Stock Inventory from CSV Importing Inventory 
 Import Inventory By Product import stock with lot number import inventory with lot number import lot with stock import stock balance import stock data import odoo stock import data on odoo
update import adjustment update lot stock update stock adjustment update inventory stock adjustment import lot with inventory adjustment
import stock with lot number import stock with product details update stock with product.

    """,
    "license" : "OPL-1",
    "depends" : ['base','stock','sale_management','purchase','account'],
    "data": [
        'wizard/import_wizard.xml',
        'wizard/validation.xml',
    ],
    'installable': True,
    'auto_install': False,
    'price': 12,
    'currency': "EUR",
    'category': 'Warehouse',
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
