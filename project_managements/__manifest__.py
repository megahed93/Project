{
    'name': 'Project Management',
    'version': '15.0.1.0.0',
    'summary': 'Manage projects and tasks with detailed tracking',
    'description': """
        A module to manage projects and tasks in Odoo. 
        Features include task creation, modification, project management, 
        tracking task progress, adding comments, history tracking, and file attachments.
    """,
    'author': 'Engineer',
    'category': 'Project',
    'depends': ['base', 'mail'],
    'data': [
        'views/project_task_view.xml',
        'views/project_view.xml',
        'views/history_tracking_view.xml',
        'data/project_data.xml',
        'data/mail_template_data.xml',
        'data/cron_job_data.xml',  # Adding cron job for daily update
    ],
    'installable': True,
    'application': True,
'images': [
    'static/description/cover.png'  # صورة الغلاف
    'static/description/icon.png',  # الأيقونة
],
}
