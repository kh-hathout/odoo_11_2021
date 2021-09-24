from odoo import api, models
class CancelMultiPicking(models.TransientModel):
    _name = "cancel.multi.picking"
    _description = "Cancel Multi Delivery"

    @api.multi
    def action_cancel(self):
        pickings = self.env.context.get('active_ids')
        cancel_pickings = self.env['stock.picking'].browse(pickings)
        res = True
        for cancel_picking in cancel_pickings:
            res = cancel_picking.with_context(Flag=True).action_cancel()
        return res
