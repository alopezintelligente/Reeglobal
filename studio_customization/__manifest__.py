# -*- coding: utf-8 -*-
{
    'name': 'Studio customizations',
    'version': '14.0.1.0',
    'category': 'Studio',
    'description': u"""
This module has been generated by Odoo Studio.
It contains the apps created with Studio and the customizations of existing apps.
""",
    'author': 'Reeglobal',
    'depends': [
        'account',
        'base',
        'mrp',
        'product',
        'purchase',
        'purchase_stock',
        'sale',
        'sale_stock',
        'stock',
        'stock_account',
        'web_studio',
    ],
    'data': [
        'data/report_paperformat.xml',
        'data/ir_model.xml',
        'data/ir_model_fields.xml',
        'data/ir_ui_view.xml',
        'data/ir_actions_act_window.xml',
        'data/ir_actions_report.xml',
        'data/ir_ui_menu.xml',
        'data/ir_model_access.xml',
        'data/ir_default.xml',
    ],
    'application': False,
    'license': 'OPL-1',
}
