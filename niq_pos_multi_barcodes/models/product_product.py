# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


from odoo import api, fields, models, _
from odoo.exceptions import UserError

class ProductProduct(models.Model):

    _inherit = 'product.product'

    barcode_ids = fields.One2many(
        comodel_name="product.multi.barcode",
        inverse_name="product_id",
        string="Multi Barcode"
    )

    @api.model
    def compute_multi_barcode_product_domain(self, args):
        """
        :param args: original args
        :return: new arguments that allow search more multi barcode object
        """
        domain = []
        for arg in args:
            if isinstance(arg, (list, tuple)) and arg[0] == 'barcode':
                domain += ['|', ('barcode_ids.name', arg[1], arg[2]), arg]
            else:
                domain += [arg]
        return domain

    @api.model
    def search(self, args, offset=0, limit=0, order=None, count=False):
        new_args = self.compute_multi_barcode_product_domain(args)
        return super(ProductProduct, self).search(
            new_args, offset, limit, order, count
        )

    @api.model
    def create(self, vals):
        return super(ProductProduct, self).create(vals)

    @api.constrains('barcode')
    def check_uniqe_name(self):
        for rec in self:
            domain = [('name', '=', rec.barcode)]
            count = self.env['product.multi.barcode'].search_count(domain)
            if count:
                raise UserError(
                    'Multi barcode should be unique !.'
                    'There is an same barcode on multi-barcode tab.'
                    'Please check again !')
