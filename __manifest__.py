# -*- coding: utf-8 -*-
{
    'name': "blibrary",

    'summary': """Brussels library management module""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Ros Krotov",
    'website': "https://route.in.ua",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/10.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Test_module',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}