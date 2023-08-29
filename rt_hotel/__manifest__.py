# -*- coding: utf-8 -*-
{
    'name': "Hotel",
    'summary': """
        Sistema de Gestión de un Hotel""",
    'description': """
        Sistema que permite gestionar un hotel desde la perspectiva de Odoo
    """,
    'author': "Rapitech",
    # 'website': "https://www.rapitech.com",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Technical',
    'version': '1.0',
    'application': True,
    'sequence': '-1',
    # any module necessary for this one to work correctly
    'depends': ['base'],
    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/menus.xml',
        'views/rt_habitacion_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
}
