{
    "name": "Project Forecast Task Planning",
    "summary": "Adds missing functionality to project_forecast module.",
    "description": """    
    Module's functionality:
    * Adds option to assign shifts to tasks.
    * Allows to group by tasks on shift views.
    * Allows to see forecasted hours for each task.
    * Adds task to shift notification.
    """,
    "author": "myOdoo.pl",
    "website": "https://myodoo.pl",
    "category": "Project Management",
    "version": "19.0.1.0.0",
    "depends": [
        "project",
        "planning",
        "project_forecast",
        "planning_holidays"
    ],
    "data": [
        "views/planning_views.xml",
        "views/planning_template_views.xml",
        "views/planning_templates.xml",
        "views/project_views.xml",
    ],
    'license': 'LGPL-3',
    'images': ['static/description/banner.png'],
    "installable": True,
    "auto_install": False,
}
