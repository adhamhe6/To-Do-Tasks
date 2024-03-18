{
    'name': 'To-Do Task',
    'description': """
    Odoo To Do Task Management System """,
    'author': "Adham",
    'version': '1.0',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/menus.xml',
        'demo/todo_task_demo.xml',
    ],
    'demo':[
        'demo/todo_task_demo.xml',
    ],
    'demo': [],
    'application': True,
    'installable': True,
    'sequence': 6,
    
}