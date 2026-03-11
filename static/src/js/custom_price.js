/** @odoo-module **/

import {rpc} from "@web/core/network/rpc";

import publicWidget from "@web/legacy/js/public/public_widget";


publicWidget.registry.CustomAddToCart = publicWidget.Widget.extend({
    selector: '.oe_website_sale',  // The parent container

    events: {
        'click #custom_add_to_cart': '_onClickAddToCart',
    },

    async _onClickAddToCart(ev) {
        ev.preventDefault();

        const button = ev.currentTarget;
        const productTemplateId = button.dataset.productTemplateId;

        const productIdInput = document.querySelector('.product_id');
        const productId = productIdInput ? parseInt(productIdInput.value) : null;

        const minFixed = parseInt(button.dataset.minFixed, 10);
        const minPercent = parseInt(button.dataset.minPercent, 10);
        const maxPrice = parseInt(
            document.querySelector('.js_product_price')?.dataset.maxPrice || 0
        );


        const currencySymbol = button.dataset.currencySymbol;

        var qty = document.querySelector('.quantity')?.value || 1;

        const alertBox = document.getElementById('date_overlap_alert');
        const priceInput = document.querySelector('.js_custom_price');
        const percentInput = document.querySelector('.js_custom_percent');


        const showError = (message) => {
            alertBox.textContent = message;
            alertBox.classList.remove('d-none');
        };


        let dynamic_price = 0;

        if (priceInput && priceInput.value) {

            dynamic_price = parseFloat(priceInput.value);

            if (dynamic_price > maxPrice) {
                showError(`Maximum amount is ${currencySymbol} ${maxPrice}`);
                return;

            }

            if (dynamic_price < minFixed) {
                showError(`Minimum amount is ${currencySymbol} ${minFixed}`);
                return;
            }
        } else if (percentInput && percentInput.value) {
            dynamic_price = parseFloat(percentInput.value);


            if (dynamic_price > maxPrice) {
                showError(`Maximum amount is ${currencySymbol} ${maxPrice}`);
                return;

            }

            if (dynamic_price < minPercent) {
                showError(`Minimum amount is ${currencySymbol} ${minPercent}`);
                return;
            }
        }

        await rpc("/shop/cart/add", {
            product_template_id: productTemplateId,
            product_id: parseInt(productId),
            quantity: qty,
            dynamic_price: dynamic_price,
        });

        window.location.href = "/shop/cart";

    },
});
