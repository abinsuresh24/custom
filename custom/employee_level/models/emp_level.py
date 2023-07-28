# -*- coding: utf-8 -*-
from odoo import fields, models


class EmpLevel(models.Model):
    _name = "emp.level"
    _description = "Details about employee level"
    _rec_name = "employee_level"

    employee_level = fields.Char(string="Employee level")
    employee_salary = fields.Float(string="Salary")
