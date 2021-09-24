========================
Stock Restrict Locations
========================
Restricted access to warehouses, locations, and picking types on a per-user basis.


Installation
============
This module does not require any external Python or binary dependencies. Simply drop :code:`stock_restrict_locations` in your addons folder, and install.

`See here <https://odoo-development.readthedocs.io/en/latest/odoo/usage/install-module.html#from-zip-archive>`_ for a more detailed Odoo module install guide.


Configuration
=============
Restrictions are setup per-user:

1. Browse to :code:`Settings -> Users -> Your User` 
2. Under the :code:`Applications` heading, set the :code:`Inventory: User` permission
3. Enable the module by checking :code:`Restrict Warehouses/Locations`
4. Select the warehouses, locations, and picking types for your user
5. All done!


Notes
=====

Please note that this module applies restrictions to ALL of the following records:

* :code:`stock.warehouse`
* :code:`stock.location`
* :code:`stock.picking.type`
* :code:`stock.picking` via :code:`location_id` or :code:`location_dest_id`
* :code:`stock.move` via :code:`location_id` or :code:`location_dest_id`
* :code:`stock.quant` via :code:`location_id`
* :code:`stock.inventory` via :code:`location_id`
* :code:`stock.inventory.line` via :code:`location_id`
* :code:`stock.orderpoint` via :code:`location_id`


If your use-case requires additional restrictions, I would be happy to add them in. Simply visit my `contact page <https://www.ryanc.me/contact>`_ to get in touch.


Also please note that some built-in Odoo modules (namely point_of_sale) require certain picking types and locations to function correctly. Please test thoroughly before publishing to a production environment. For example, the :code:`Point of Sale` module requires the following to function correctly:

* The :code:`PoS Orders` route
* The PoS' location (e.g. :code:`WH/Stock`)
* :code:`Physical Locations`
* :code:`Partner Locations/Customers`
* Possibly others for certain use-case