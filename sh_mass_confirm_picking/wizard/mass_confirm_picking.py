# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.

from odoo import models, fields, api, _


class MassConfirmPicking(models.TransientModel):
    _name = 'mass.confirm.picking'
    _description = 'Mass Confirm Picking'

    message = fields.Text(string='Message', readonly=True)
    compute_message = fields.Text(string='Message', readonly=True)

    @api.model
    def default_get(self, fields):
        res = super(MassConfirmPicking, self).default_get(fields)
        active_ids = self._context.get('active_ids')
        sale_orders = self.env['sale.order'].browse(active_ids)
        order_list = []
        draft_orders = []
        for order in sale_orders:
            if order.state in ['sale']:
                order_list.append(order.name)
            elif order.state not in ['sale']:
                draft_orders.append(order.name)
        msg = ','.join(order_list)
        message = ','.join(draft_orders)
        res.update({
            'message': "Validate The Following Sale Orders" + " " + msg,
            })
        if len(draft_orders) > 0:
            res.update({
                'compute_message': "Following Orders are not Confirmed" + " " + message
                })
        return res

    @api.multi
    def action_confirm_picking(self):
        if self.env.context.get('active_ids', False):
            done_picking = []
            not_done_picking = []
            for order in self.env['sale.order'].search([('id', 'in', self.env.context.get('active_ids', False))]):
                if order.state in ['sale']:
                    if order.picking_ids:
                        for picking in order.picking_ids:
                            if picking.state in ['done']:
                                not_done_picking.append(picking.name)
                            else:
                                for move in picking.move_lines:
                                    if move.product_id.qty_available > 0.0:
                                        if picking.name not in done_picking:
                                            done_picking.append(picking.name)
                                        picking.action_confirm()
                                        picking.action_assign()
                                        picking.button_validate()
                                        wiz = self.env['stock.immediate.transfer'].create({'pick_ids': [(4, picking.id)]})
                                        wiz.process()
                                    else:
                                        if picking.name not in not_done_picking:
                                            not_done_picking.append(picking.name)
            msg = ""
            if len(done_picking) > 0:
                msg = "Following Picking Validated Successfully" + " " + ','.join(done_picking)
            message = ""
            if len(not_done_picking) > 0:
                message = "There is some issue to validate following Picking" + " " + ','.join(not_done_picking)

            return {
                'name': _('Picking Validate Success'),
                'type': 'ir.actions.act_window',
                'res_model': 'picking.warning.message',
                'view_type': 'form',
                'view_mode': 'form',
                'context': {'default_message': msg, 'default_compute_message': message},
                'target': 'new'
            }
