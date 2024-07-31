{
    'name': 'Project Management',
    'version': '15.0.1.0.0',
    'summary': 'Manage projects and tasks with detailed tracking',
    'description': """
    <h1>Module Description</h1>
    <p>This module offers a range of powerful features to help you manage your projects effectively:</p>
    <ul>
        <li><strong>Complete Project Control:</strong> Manage and organize your projects with ease, allowing you to track progress and achieve goals efficiently.</li>
        <li><strong>Task Assignment and Management:</strong> Assign tasks to team members based on their responsibilities and skills, ensuring proper distribution and execution.</li>
        <li><strong>Tracking Responses and Interactions:</strong> Monitor responses to tasks, allowing you to follow up and ensure tasks are completed correctly.</li>
        <li><strong>Setting Deadlines:</strong> Assign specific deadlines for tasks, helping you manage time and meet objectives within the set timeframes.</li>
        <li><strong>Task Stages:</strong> Track the stages of task completion and identify where each task stands, providing a clear view of progress and task status.</li>
    </ul>
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
        'static/description/icon.png',  # الأيقونة
        'static/description/cover.png'  # صورة الغلاف
    ],
    'license': 'OPL-1',
}
