# -*- coding: utf-8 -*-
from odoo import fields, models


class EmployeeLevel(models.Model):
    _name = "employee.level"
    _description = "Details about employee level"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = "employee_id"

    employee_id = fields.Many2one('hr.employee', string="Employee",
                                  help="Name of the employee", required=True)
    job_title = fields.Char(related="employee_id.job_title")
    department_id = fields.Many2one(related="employee_id.department_id")
    phone = fields.Char(related="employee_id.work_phone")
    email = fields.Char(related="employee_id.work_email")
    company_id = fields.Many2one(related="employee_id.company_id")
    emp_level_id = fields.Many2one("emp.level", string="Level")
    emp_salary = fields.Float(related="emp_level_id.employee_salary",
                              string="Salary")
