# -*- coding: utf-8 -*-
{
    'name': "Debrand User Menu",

    'summary': """
        This module is providing customization on user Menu         

""",

    'description': """
        This module is providing customization on user Menu         
    """,

    'author': "Amel Salah",

    'category': 'Customizations',
    'version': '16.0',
    'price' : 25,
    'currency' : 'EUR',
     'license': 'OPL-1',
    # any module necessary for this one to work correctly
    'depends': ['base' ],
     'images': ['debrand_user_menu/static/description/1.png'],

    # always loaded
    'data': [
      
        # 'views/template.xml',
 
    ], 

     'assets': {
        'web.assets_backend': [
            'debrand_user_menu/static/src/js/menu.js']}
    

}
