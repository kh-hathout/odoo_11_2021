from odoo import models, fields, api, _

class stock_picking(models.Model):    
    _inherit="stock.picking"
    
    account_invoice_ids = fields.Many2many('account.invoice',string="Account Invoice",copy=False)
    
    @api.one
    def _prepare_supplier_invoice_data(self):
        journal = self.env['account.journal'].search([('type', '=', 'purchase'), ('company_id', '=', self.company_id.id)], limit=1)
        if not journal:
            raise Warning(_('Please define purchase journal for this company: "%s" (id:%d).') % (self.company_id.name, self.company_id.id))

        context = self._context.copy()
        context['company_id'] = self.company_id.id
        vals = {'name': self.name,
            'origin': self.purchase_id.name,
            'type': 'in_invoice',
            'date_invoice': self.scheduled_date,
            'reference': self.origin,
            'partner_id': self.purchase_id.partner_id.id,
            'journal_id': journal.id,
            'currency_id': self.purchase_id.currency_id.id,
            'company_id': self.company_id.id
            }
        inv = self.env['account.invoice'].with_context(context).new(vals)
        inv._onchange_partner_id()
        new_vals = {k: v or False for k, v in dict(inv._cache).items()}
        invoice_vals = inv._convert_to_write(new_vals)
        invoice = self.env['account.invoice'].create(invoice_vals)
        new_lines = self.env['account.invoice.line']
        for line in self.purchase_id.order_line:
            data = invoice._prepare_invoice_line_from_po_line(line)
            new_line = new_lines.new(data)
            line_value = new_line._convert_to_write({name: new_line[name] for name in new_line._cache})
            invoice_line_id = new_lines.create(line_value)
            invoice_line_id._compute_price()
            invoice.write({'invoice_line_ids': [(4,invoice_line_id.id)]})
            invoice._onchange_invoice_line_ids()
            line._compute_qty_invoiced()
        self.account_invoice_ids = [(4,invoice.id)]
    
    
    @api.multi
    def action_done(self):
        result=super(stock_picking,self).action_done()
        for picking in self:
            if picking and picking.sale_id:
                partner_location = self.env.ref('stock.stock_location_customers').id
                if picking.location_dest_id.id == partner_location:
                    inv_id = picking.sale_id.action_invoice_create()
                    invoice_obj = self.env['account.invoice'].browse(inv_id)
                    self.account_invoice_ids = [(4,invoice_obj.id)] 
            elif picking and picking.purchase_id:
		vendor_location = self.env.ref('stock.stock_location_suppliers').id
                if picking.location_id.id == vendor_location:
                    picking._prepare_supplier_invoice_data()
        return result 
    
    @api.multi
    def action_view_account_invoice(self):
        if self.sale_id:
            invoices = self.mapped('account_invoice_ids')
            action = self.env.ref('account.action_invoice_tree1').read()[0]
            if len(invoices) > 1:
                action['domain'] = [('id', 'in', invoices.ids)]
            elif len(invoices) == 1:
                action['views'] = [(self.env.ref('account.invoice_form').id, 'form')]
                action['res_id'] = invoices.ids[0]
            else:
                action = {'type': 'ir.actions.act_window_close'}
            return action
        elif self.purchase_id:
            action = self.env.ref('account.action_invoice_tree2')
            result = action.read()[0]
            if self.purchase_id:
                result['context'] = {'type': 'in_invoice', 'default_purchase_id': self.purchase_id.id}
            if self.sale_id:
                result['context'] = {'type': 'out_invoice', 'default_sale_id': self.sale_id.id}
    
            if not self.account_invoice_ids:
                journal_domain = [
                    ('type', '=', 'purchase'),
                    ('company_id', '=', self.company_id.id),
                    ('currency_id', '=', self.purchase_id.currency_id.id),
                ]
                default_journal_id = self.env['account.journal'].search(journal_domain, limit=1)
                if default_journal_id:
                    result['context']['default_journal_id'] = default_journal_id.id
            else:
                # Use the same account journal than a previous invoice
                result['context']['default_journal_id'] = self.account_invoice_ids.journal_id.id
    
            if len(self.account_invoice_ids) != 1:
                result['domain'] = "[('id', 'in', " + str(self.account_invoice_ids) + ")]"
            elif len(self.account_invoice_ids) == 1:
                res = self.env.ref('account.invoice_supplier_form', False)
                result['views'] = [(res and res.id or False, 'form')]
                result['res_id'] = self.account_invoice_ids.id
            return result
        
