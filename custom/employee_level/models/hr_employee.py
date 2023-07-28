# -*- coding: utf-8 -*-
from odoo import fields, models


class HrEmployee(models.Model):
    _inherit = "hr.employee"
    _description = "Inherited employee model"

    emp_salary = fields.Float(string="Salary")
    employee_level_id = fields.Many2one('employee.level')

    def action_promote(self):
        print("promote")
        emp = self.env['employee.level'].search([('employee_id', '=', self.id)])
        print(emp)
        salary = self.env['emp.level'].search([])
        print(salary, "salary")
        print(self.id)
        self.emp_salary = emp.emp_salary
        # sal = salary.mapped('employee_level')
        # print(sal, "sal")
        sorted_salary = salary.sorted(key=lambda r: r.employee_salary)
        print('aa', sorted_salary)
        emp.write({'emp_level_id': salary[1]})
