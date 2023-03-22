from odoo import models, fields


class EmployeeLevel(models.Model):
    _name = 'employee.level'
    _description = 'Employee level'
    _rec_name = 'level'

    level = fields.Integer()
    salary = fields.Integer()
