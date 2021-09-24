# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2015 DevIntelle Consulting Service Pvt.Ltd (<http://devintellecs.com>).
#
##############################################################################

from odoo import fields, models

class Company(models.Model):
    _inherit = 'res.company'

    po_tripple_validation = fields.Selection([
        ('two_step', 'Confirm Purchase Order in two step'),
        ('three_step', 'Get 3 levels of approvals to confirm a Purchase Order')
        ], string="Levels of Approvals", default='two_step',
        help="Provide a triple validation mechanism for Purchase Order")

    po_tripple_validation_amount = fields.Monetary(string='Triple validation Amount', default=5000,
        help="Minimum amount for which a triple validation is required")

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: