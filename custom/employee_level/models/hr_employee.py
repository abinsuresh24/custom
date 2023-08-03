# -*- coding: utf-8 -*-
from odoo import fields, models
from odoo.exceptions import MissingError


class HrEmployee(models.Model):
    _inherit = "hr.employee"
    _description = "Inherited employee model"

    employee_level_id = fields.Many2one('emp.level')
    emp_salary = fields.Float(related="employee_level_id.employee_salary",
                              string="Salary")
    maximum_salary = fields.Boolean(string="Maximum salary")

    def action_promote(self):
        if not self.employee_level_id:
            raise MissingError("Please select a Employee level for promote")
        else:
            order = self.env['emp.level'].search([])
            sal_level = order.mapped('employee_salary')
            if self.employee_level_id.employee_salary == sal_level[0]:
                next_level = self.env['emp.level'].search(
                    [('employee_salary', '=', sal_level[1])])
                self.write({"employee_level_id": next_level})
            else:
                next_level = self.env['emp.level'].search(
                    [('employee_salary', '=', sal_level[2])])
                self.write({"employee_level_id": next_level})
                self.maximum_salary = True
