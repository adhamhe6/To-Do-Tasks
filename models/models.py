from odoo import models, fields


class TodoTask(models.Model):

    _name = 'todo.task'
    _description = 'To-Do Task Manager'
    _order = 'is_completed, create_date DESC'

    name = fields.Char(string='Task Name', required=True)
    description = fields.Text(string='Description')
    is_completed = fields.Boolean(string='Completed', default=False)
