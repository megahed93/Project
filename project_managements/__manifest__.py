import os

def read_description(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

MODULE_DESCRIPTION_FILE = os.path.join(os.path.dirname(__file__), 'static/description/module_description.html')

{
    'name': 'Project Management',
    'version': '15.0.1.0.0',
    'summary': 'Manage projects and tasks with detailed tracking',
 'description': read_description(MODULE_DESCRIPTION_FILE),

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
