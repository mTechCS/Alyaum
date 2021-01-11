# -*- coding: utf-8 -*-
# from odoo import http


# class HcsPayrollReport(http.Controller):
#     @http.route('/hcs_payroll_report/hcs_payroll_report/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hcs_payroll_report/hcs_payroll_report/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hcs_payroll_report.listing', {
#             'root': '/hcs_payroll_report/hcs_payroll_report',
#             'objects': http.request.env['hcs_payroll_report.hcs_payroll_report'].search([]),
#         })

#     @http.route('/hcs_payroll_report/hcs_payroll_report/objects/<model("hcs_payroll_report.hcs_payroll_report"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hcs_payroll_report.object', {
#             'object': obj
#         })
