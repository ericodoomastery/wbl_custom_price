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
from odoo.http import request, route
from odoo.addons.website_sale.controllers.cart import Cart


class CustomCart(Cart):
    @route(
        route='/shop/cart/add',
        type='jsonrpc',
        auth='public',
        methods=['POST'],
        website=True,
        sitemap=False
    )
    def add_to_cart(
            self,
            product_template_id,
            product_id,
            quantity=None,
            uom_id=None,
            product_custom_attribute_values=None,
            no_variant_attribute_value_ids=None,
            linked_products=None,
            dynamic_price=None,
            **kwargs
    ):
        response = super(Customcart, self).add_to_cart(
            product_template_id=product_template_id,
            product_id=product_id,
            quantity=quantity,
            uom_id=uom_id,
            product_custom_attribute_values=product_custom_attribute_values,
            no_variant_attribute_value_ids=no_variant_attribute_value_ids,
            linked_products=linked_products,
            dynamic_price=dynamic_price,
            **kwargs)
        order = request.cart
        order_line = order.order_line.filtered(lambda line: line.product_id.id == product_id)

        if dynamic_price:
            order_line.write({
                'price_unit': float(dynamic_price),
                'dynamic_price': float(dynamic_price),
                'is_custom_price': True,

            })
        else:
            order_line.write({
                'is_custom_price': False,
            })

        return response
