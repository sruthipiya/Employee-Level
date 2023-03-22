{
    'name': 'Employee Level',
    'category': 'Employee',
    'summary': 'Employee level',
    'sequence': -1,
    'installable': True,
    'application': True,
    'depends': ['base', 'hr'],
    'data': ['security/ir.model.access.csv',
             'views/employee_level.xml',
             'views/employee_configuration.xml',
             'views/employee_menu.xml']
}
