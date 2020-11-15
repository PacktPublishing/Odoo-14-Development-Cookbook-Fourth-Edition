odoo.define('pos_demo.custom', function (require) {
    "use strict";

    var core = require('web.core');
    var rpc = require('web.rpc');
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

    var lastOrders = screens.ActionButtonWidget.extend({
        template: 'LastOrders',
        button_click: function () {
            var self = this;
            var order = this.pos.get_order();
            if (order.attributes.client) {
                var domain = [['partner_id', '=', order.attributes.client.id]];
                rpc.query({
                    model: 'pos.order',
                    method: 'search_read',
                    args: [domain, ['name', 'amount_total', 'cu']],
                    kwargs: { limit: 5 },
                }).then(function (orders) {
                    if(orders.length > 0){
                        var order_list = _.map(orders, function (o) {
                            return { 'label': _.str.sprintf("%s - TOTAL: %s", o.name, o.amount_total) };
                        });
                        self.show_order_list(order_list);
                    } else {
                        self.show_error('No previous order found for the customer');
                    }
                });
            } else {
                this.show_error('Please select the customer');
            }
        },
        show_order_list: function(list) {
            this.gui.show_popup('selection', {
                'title': 'Last 5 orders',
                'list': list,
                'confirm': function (reward) {
                    order.apply_reward(reward);
                },
            });
        },
        show_error: function (message){
            this.gui.show_popup('error', {
                title: "Warning",
                body: message,
            });
        }
    });

    screens.define_action_button({
        'name': 'last_orders',
        'widget': lastOrders
    });

});