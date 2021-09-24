from odoo import api, fields, models, _


class validation_records(models.TransientModel):
    _name = 'import.validation'

    name = fields.Char(string="Name")

    validation_ids = fields.One2many('import.validation.line','validation_id',string="Validation Lines")




class validation_records(models.TransientModel):
    _name = 'import.validation.line'


    element = fields.Char(string="Validation Error")
    validation_id = fields.Many2one()
