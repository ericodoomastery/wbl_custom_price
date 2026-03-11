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
from odoo import api, fields, models

class Product(models.Model):
    _inherit = 'product.template'

    custom_price = fields.Boolean(required=True)


    min_custom_price = fields.Selection(
        [
            ('fixed', 'Fixed Price'),
            ('percent', 'Percentage'),
        ],
        required=True,
        default='fixed',
    )

    min_fixed_price = fields.Float('Set Minimum Fixed Price', requierd=True)
    min_percent_price = fields.Float('Set Minimum Percentage', requierd=True)
    estimated_price = fields.Char(compute='_compute_show_min_percent')

    final_price = fields.Float('final')


    @api.depends('min_percent_price', 'list_price')
    def _compute_show_min_percent(self):
        for product in self:
            if product.min_percent_price and product.list_price:
                estimated = product.list_price * (
                         product.min_percent_price / 100
                )
                final = estimated
                product.final_price =  round(final, 2)
                product.estimated_price = f"(= $ {final:.2f} Estimated Price)"
            else:
                product.estimated_price = ''
