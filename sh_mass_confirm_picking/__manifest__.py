# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.

{
    "name": "Mass Confirm Picking",
    "author": "Softhealer Technologies",
    "website": "https://www.softhealer.com",
    "support": "support@softhealer.com",
    "category": "Sales",
    "summary": " Multiple Picking Mass Action App, Mass Conform Quote, Mass Validate Delivery Order,  Mass Validate Sales Order, Bunch Validate Quotation Module, Sales Order Pack Validate, Mass Confirm SO Odoo",
    "description": """
When you have bulk sale orders then it's very difficult to validate every picking one by one. This module provides functionality to validate all sale orders in a single click. The user has to select the sale orders from the list view and then validate all pickings. It shows notification in success & any issue in the validation. It shows a warning if not conformed sale orders.
 Mass Confirm Picking Odoo
 Multiple Picking Mass Action Module, Mass Validate Sales Order, Bunch Validate Quotation, Sales Order Pack Validate, Mass Conform Quote, Mass Validate Delivery Order, Mass Confirm SO Odoo
 Multiple Picking Mass Action App, Mass Conform Quote, Mass Validate Delivery Order,  Mass Validate Sales Order, Bunch Validate Quotation Module, Sales Order Pack Validate, Mass Confirm SO Odoo

                    """,
    "version": "11.0.1",
    "depends": ["base", "sale_management", "stock"],
    "application": True,
    "data": [
            "wizard/mass_confirm_picking.xml",
            "wizard/picking_warning_message.xml",
            ],
    "images": ["static/description/background.png", ],
    "live_test_url": "https://youtu.be/25LHDBFqbe0",
    "auto_install": False,
    "installable": True,
	"price": "35",
	"currency": "EUR"
}
