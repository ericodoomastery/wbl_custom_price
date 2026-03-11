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
from odoo import models, fields, api


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    is_custom_price = fields.Boolean('Is Custom Price')
    dynamic_price = fields.Float('Dynamic Price')

    @api.depends('product_id', 'product_uom_id', 'product_uom_qty')
    def _compute_price_unit(self):
        def has_manual_price(line):
            # `line.currency_id` can be False for NewId records
            currency = (
                    line.currency_id
                    or line.company_id.currency_id
                    or line.env.company.currency_id
            )
            return currency.compare_amounts(line.technical_price_unit, line.price_unit)

        force_recompute = self.env.context.get('force_price_recomputation')
        for line in self:
            # Don't compute the price for deleted lines or lines for which the
            # price unit doesn't come from the product.
            if not line.order_id or line.is_downpayment or line._is_global_discount():
                continue

            # check if the price has been manually set or there is already invoiced amount.
            # if so, the price shouldn't change as it might have been manually edited.
            if (
                    (not force_recompute and has_manual_price(line))
                    or line.qty_invoiced > 0
                    or (line.product_id.expense_policy == 'cost' and line.is_expense)
            ):
                continue
            line = line.with_context(sale_write_from_compute=True)

            if not line.is_custom_price and not line.product_id:
                if not line.product_uom_id or not line.product_id:
                    line.price_unit = 0.0

                    line.technical_price_unit = 0.0
                else:
                    line._reset_price_unit()


    def _get_cart_display_price(self):
        self.ensure_one()

        price_type = (
            'price_subtotal'
            if self.order_id.website_id.show_line_subtotals_tax_selection == 'tax_excluded'
            else 'price_total'
        )

        if self.product_type == 'combo' and self.is_custom_price and self.dynamic_price:
            taxes = self.tax_ids.compute_all(
                self.dynamic_price,
                self.currency_id,
                self.product_uom_qty,
                product=self.product_id,
                partner=self.order_partner_id,
            )

            return (
                taxes['total_excluded']
                if price_type == 'price_subtotal'
                else taxes['total_included']
            )

        # Default Odoo behavior
        return sum(self._get_lines_with_price().mapped(price_type))