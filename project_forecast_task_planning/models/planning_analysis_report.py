# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api


class PlanningAnalysisReport(models.Model):
    _inherit = "planning.analysis.report"

    task_id = fields.One2many('project.task', string='Task', compute='_compute_task_id',
                              search='_search_task_id')

    def _compute_task_id(self):
        for slot in self:
            slot.task_id = slot.task_id

    @api.model
    def _search_task_id(self, operator, value):
        return [('task_id', operator, value)]
