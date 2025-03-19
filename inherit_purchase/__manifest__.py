# -*- coding: utf-8 -*-
{
    'name': 'Inherit_purchase',
    'version': '17.0.1.0.0',
    'summary': """ Inherit_purchase Summary for test """,
    'author': '',
    'website': '',
    'category': '',
    'depends': ['base', 'web','purchase'],
    "data": [
        # "views/purchase_order_line_views.xml"
    ],
    'assets': {
              'web.assets_backend': [
                  'inherit_purchase/static/src/**/*'
              ],
          },
    'application': True,
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
