import os

def get_description():
    file_path = os.path.join(os.path.dirname(__file__), 'static/description/description.html')
    with open(file_path, 'r') as file:
        return file.read()

{
    'name': 'Project Management',
    'version': '15.0.1.0.0',
    'summary': 'Manage projects and tasks with detailed tracking',
    'description': get_description(),
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
        'static/description/icon.png',  # الأيقونة
        'static/description/cover.png'  # صورة الغلاف
    ],
    'license': 'OPL-1',
}
