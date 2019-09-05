# -*- coding: utf-8 -*-

{
    'name': "Descarga E3L",

    'summary': """
        Módulo para añadir como anexo un xml en formato E3L del DI""",

    'description': """
        Módulo para añadir como anexo un xml en formato E3L del DI
    """,

    'author': "Pedro Baños Guirao",
    'website': "https://ingenieriacloud.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Tools',
    'version': '2.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        #'security/ir.model.access.csv',
        #'views/connector_miteco_view.xml',
        #'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'installable': True,
    'application': True,
    'auto_install': False,
}