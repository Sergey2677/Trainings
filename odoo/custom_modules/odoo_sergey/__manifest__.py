# -*- coding: utf-8 -*-
{
    'name': "Odoo_sergey",
    'summary': """""",
    'description': """""",
    'author': "sergeyasdf2677",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['sale'],

    # always loaded
    'data': [
        'views/sale_order_view.xml',
        'report/custom_print_template.xml',
    ],
    # only loaded in demonstration mode
    'demo': [],
}
