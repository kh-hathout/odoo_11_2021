# Copyright 2020 CorTex IT Solutions Ltd. (<https://cortexsolutions.net/>)
# License OPL-1

from odoo import models, api


class MultiSaleConfirmWizard(models.TransientModel):
    _name = 'multi.sale.confirm.wizard'

    @api.multi
    def confirm_multi_sale(self):
        sales = self.env['sale.order'].browse(self._context.get('active_ids')).filtered(lambda x: x.state not in ('done', 'cancel'))
        if sales:
            for sale in sales:
                sale.action_confirm()
