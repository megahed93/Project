from odoo import models, fields, api

class ProjectTaskHistory(models.Model):
    _name = 'project.task.history'
    _description = 'Task History'

    task_id = fields.Many2one('project.task', string='Task', required=True)
    note = fields.Text(string='Note')
    created_at = fields.Datetime(string='Created At', default=fields.Datetime.now)

    @api.model
    def create(self, vals):
        history = super(ProjectTaskHistory, self).create(vals)
        if history.note:
            history.task_id._send_comment_email(history.note)
        return history
