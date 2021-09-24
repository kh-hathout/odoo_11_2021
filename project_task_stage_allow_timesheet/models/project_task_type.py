# Copyright 2018 ACSONE SA/NV
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ProjectTaskType(models.Model):

    _inherit = 'project.task.type'

    allow_timesheet = fields.Boolean(
        string="Allow timesheets",
        default=True,
    )
