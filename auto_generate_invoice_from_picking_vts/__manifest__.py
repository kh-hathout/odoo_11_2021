{
    # App information

    'name': 'Auto Invoice When Validate Delivery/Incoming Shipment',
    'version': '11.0',
    'category': 'Accounting',
    'summary': 'Auto Create Invoice when Validate Delivery Order/Incoming Shipment',
    
    # Dependencies

    'depends': ['purchase','sale','stock'],

    # Views

    'data': [
        'view/stock_picking.xml',
        ],

    # Odoo Store Specific

    'images': ['static/description/auto_inv.png'],

    'author': 'Vraja Technologies',

    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'price': '29' ,
    'currency': 'EUR',
    'license': 'OPL-1',
}
