# -*- coding: utf-8 -*-
{
    'name': "tts_modifier_accounting",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','account', 'tts_internal_transfer','tuanhuy_invoice','tuanhuy_sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/account_account_view.xml',
        'views/sale_gross_proifit.xml',
        'views/customer_invoice_view.xml',
        'views/sale_order_view.xml'
    ],
    # only loaded in demonstration mode
    'qweb': [
        'static/src/xml/*.xml',
    ],
}