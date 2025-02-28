# -*- coding: utf-8 -*-

from odoo import api, fields, models


class PlanningAnalysisReport(models.Model):
    _inherit = "planning.analysis.report"

    task_id = fields.Many2one("project.task", string="Task")

    @api.model
    def _select(self):
        res = super(PlanningAnalysisReport, self)._select()
        select_new = """
        , S.task_id AS task_id
        """
        res += select_new
        return res
