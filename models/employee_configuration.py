from odoo import models, fields
from odoo.exceptions import ValidationError


class EmployeeConfiguration(models.Model):
    _inherit = 'hr.employee'

    def _default_employee_level(self):
        return self.env['employee.level'].search(['level', '=', '1'])

    employee_level_id = fields.Many2one('employee.level', default='_default_employee_level')
    employee_salary = fields.Integer(related='employee_level_id.salary')
    flag = fields.Integer(default=0)

    def action_promote(self):
        # emp = self.env['employee.level'].search([])[-1]
        # print(self.employee_level_id.id, emp.id)
        # if self.employee_level_id.id == emp.id - 1:
        # if self.env['employee.level'].search([]):
        employee_rec = self.env['employee.level'].search([('level', '>', self.employee_level_id.level)]).sorted('level')
        last_index = employee_rec[-1]
        if self.employee_level_id.id == last_index.id - 1:
            self.flag = 1
        self.employee_level_id = employee_rec[0]
        print(employee_rec[0])

        # else:
        #     raise ValidationError('Add a level')

        # print(emp)


