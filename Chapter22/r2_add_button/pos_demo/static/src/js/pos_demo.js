odoo.define('pos_demo.custom', function (require) {
    "use strict";

    var screens = require('point_of_sale.screens');

    var discount_button = screens.ActionButtonWidget.extend({
        template: 'BtnDiscount',
        button_click: function () {
            var order = this.pos.get_order();
            if (order.selected_orderline) {
                order.selected_orderline.set_discount(5);
            }
        }
    });

    screens.define_action_button({
        'name': 'discount_btn',
        'widget': discount_button
    });

});