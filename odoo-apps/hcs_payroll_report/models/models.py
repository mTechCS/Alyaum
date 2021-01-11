# -*- coding: utf-8 -*-

from odoo import models, fields, api


class hr_payslip(models.Model):
    _inherit = 'hr.payslip'

    
    def _get_salary_line_total(self, code):
        total = 0.0
        for line in self.line_ids:
            if line.code == code:
                total += line.total
            elif code == 'custom_total':
                if line.code in ['HRA', 'TRA', 'ORT', 'MBL','CR','FDL','OHA']:
                    total += line.total
            elif code == 'custom_total_d':
                if line.code in ['LO', 'GOSI', 'PNL', 'OD']:
                    total += line.total
            else:
                continue
        return total
    
    def _get_deserve(self,sub_total):
        for rec in self:
            rec.sub_total = self._get_salary_line_total('BASIC') / 30 * self.worked_days_line_ids.number_of_days
            return rec.sub_total


