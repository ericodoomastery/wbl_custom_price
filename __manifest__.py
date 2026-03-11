# -*- coding: utf-8 -*-
#
#################################################################################
# Author      : Weblytic Labs Pvt. Ltd. (<https://store.weblyticlabs.com/>)
# Copyright(c): 2023-Present Weblytic Labs Pvt. Ltd.
# All Rights Reserved.
#
#
# This program is copyright property of the author mentioned above.
# You can`t redistribute it and/or modify it.
##################################################################################
{
    'name': 'Custom Price 1',
    'version': '19.0.1.0.0',
    'description': """website custom pricing, dynamic pricing module,  minimum price control, flexible pricing app, negotiable price module, customer defined price, donation product module, user input price,  percentage pricing,  fixed minimum price, ecommerce price control, website price validation, sales order custom price, product variant pricing, dynamic price website, pricing flexibility, custom amount product, pricing management module, website sales integration, custom checkout price, configurable product price, frontend price input,  minimum order price control, ecommerce pricing solution, adjustable product price, price override with limit, controlled discount system.""",
    'summary': """website custom pricing, dynamic pricing module,  minimum price control, flexible pricing app, negotiable price module, customer defined price, donation product module, user input price,  percentage pricing,  fixed minimum price, ecommerce price control, website price validation, sales order custom price, product variant pricing, dynamic price website, pricing flexibility, custom amount product, pricing management module, website sales integration, custom checkout price, configurable product price, frontend price input,  minimum order price control, ecommerce pricing solution, adjustable product price, price override with limit, controlled discount system.""",
    'category': 'eCommerce',
    'author': 'Weblytic Labs',
    'company': 'Weblytic Labs',
    'website': 'https://store.weblyticlabs.com',
    'price': '35.00',
    'currency': 'USD',
    'depends': ['base', 'mail', 'website', 'website_sale', 'payment', 'sale_management'],
    'data': [
        'views/product_variant_views.xml',
        'views/product_template_views.xml',
        'views/template.xml',
        'views/cart.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'wbl_custom_price/static/src/js/custom_price.js'
        ],
    },
    'images': ['static/description/banner.gif'],
    'license': 'OPL-1',
    'installable': True,
    'auto_install': False,
    'application': True,
}
