# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2015 DevIntelle Consulting Service Pvt.Ltd (<http://devintellecs.com>).
#
##############################################################################

from odoo import models, fields, api, _


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    po_tripple_verify = fields.Boolean(string="Second Approval", default=lambda self: self.env.user.company_id.po_tripple_validation == 'three_step')
    po_tripple_validation = fields.Selection(related='company_id.po_tripple_validation', string="Levels of Approvals *")
    po_tripple_validation_amount = fields.Monetary(related='company_id.po_tripple_validation_amount', string="Minimum Amount", currency_field='company_currency_id')

    def set_values(self):
        super(ResConfigSettings, self).set_values()
        self.po_tripple_validation = 'three_step' if self.po_tripple_verify else 'two_step'

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
