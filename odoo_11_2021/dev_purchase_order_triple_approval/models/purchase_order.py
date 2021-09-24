# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2015 DevIntelle Consulting Service Pvt.Ltd (<http://devintellecs.com>).
#
##############################################################################

from odoo import models, fields, api, _


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    state = fields.Selection([('draft', 'RFQ'),
                              ('sent', 'RFQ Sent'),
                              ('to approve', 'To Approve'),
                              ('second approval', 'To Second Approval'),
                              ('purchase', 'Purchase Order'),
                              ('done', 'Locked'),
                              ('cancel', 'Cancelled')],
                             string='Status', readonly=True, index=True, copy=False,
                             default='draft', track_visibility='onchange')

    @api.multi
    def button_approve(self):
        for order in self:
            if order.company_id.po_double_validation == 'two_step':
                if order.company_id.po_tripple_validation == 'two_step'\
                        or (order.company_id.po_tripple_validation == 'three_step'\
                            and order.amount_total <= self.env.user.company_id.currency_id.compute\
                            (order.company_id.po_tripple_validation_amount, order.currency_id)) or \
                        order.user_has_groups('dev_purchase_order_triple_approval.tripple_verification_po_right'):
                    return super(PurchaseOrder, self).button_approve()
                else:
                    order.write({'state': 'second approval'})
            else:
                return super(PurchaseOrder, self).button_approve()

    @api.multi
    def confirm_purchase_order(self):
        for order in self:
            return super(PurchaseOrder, self).button_approve()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
