# -*- coding: utf-8 -*-
# Copyright 2016-2018 Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    pos_allow_negative_qty = fields.Boolean(
        string='Allow Negative Quantity on PoS',
    )
