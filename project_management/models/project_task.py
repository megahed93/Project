from odoo import models, fields, api

class ProjectTask(models.Model):
    _name = 'project.task'
    _description = 'Project Task'

    name = fields.Char(string='Task Name', required=True)
    description = fields.Text(string='Description')
    user_ids = fields.Many2many('res.users', string='Assigned To')
    project_id = fields.Many2one('project.project', string='Project')
    due_date = fields.Date(string='Due Date')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
    ], string='Status', default='draft')
    history_ids = fields.One2many('project.task.history', 'task_id', string='History')
    attachment_ids = fields.One2many('ir.attachment', 'res_id', domain=[('res_model', '=', 'project.task')], string='Attachments')

    days_remaining = fields.Integer(string='Days Remaining', compute='_compute_days_remaining', store=True)
    overdue_days = fields.Integer(string='Overdue Days', compute='_compute_overdue_days', store=True)

    @api.depends('due_date')
    def _compute_days_remaining(self):
        today = fields.Date.today()
        for task in self:
            if task.due_date:
                due_date = fields.Date.from_string(task.due_date)
                task.days_remaining = (due_date - today).days
            else:
                task.days_remaining = 0

    @api.depends('due_date')
    def _compute_overdue_days(self):
        today = fields.Date.today()
        for task in self:
            if task.due_date:
                due_date = fields.Date.from_string(task.due_date)
                if today > due_date:
                    task.overdue_days = (today - due_date).days
                else:
                    task.overdue_days = 0
            else:
                task.overdue_days = 0

    @api.model
    def create(self, vals):
        task = super(ProjectTask, self).create(vals)
        # Commented out to avoid automatic "Task created" entries
        # task._create_history('Task created')
        if task.user_ids:
            task._send_assignment_email()
        return task

    def write(self, vals):
        result = super(ProjectTask, self).write(vals)
        # Commented out to avoid automatic "Task updated" entries
        # self._create_history('Task updated')
        if 'user_ids' in vals and vals['user_ids']:
            self._send_assignment_email()
        return result

    def _create_history(self, note):
        self.env['project.task.history'].create({
            'task_id': self.id,
            'note': note
        })

    def _send_assignment_email(self):
        template = self.env.ref('project_management.email_template_task_assignment')
        if template:
            for user in self.user_ids:
                template.send_mail(self.id, force_send=True, email_values={'email_to': user.email})

    def message_post(self, **kwargs):
        result = super(ProjectTask, self).message_post(**kwargs)
        if 'message_type' in kwargs and kwargs['message_type'] == 'comment':
            self._send_comment_email(kwargs['body'])
            self._create_history(kwargs['body'])  # Add this line to record the comment as history
        return result

    def _send_comment_email(self, body):
        template = self.env.ref('project_management.email_template_task_comment')
        if template:
            for user in self.user_ids:
                template.with_context(comment_body=body).send_mail(self.id, force_send=True, email_values={'email_to': user.email})

    @api.model
    def _cron_update_days_remaining(self):
        tasks = self.search([('state', '!=', 'done')])
        tasks._compute_days_remaining()
