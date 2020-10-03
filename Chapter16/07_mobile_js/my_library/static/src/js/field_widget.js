odoo.define('my_field_widget', function (require) {
"use strict";

var AbstractField = require('web.AbstractField');
var fieldRegistry = require('web.field_registry');
var mobile = require('web_mobile.core');

var core = require('web.core');

var qweb = core.qweb;


var colorField = AbstractField.extend({
    className: 'o_int_colorpicker',
    tagName: 'span',
    supportedFieldTypes: ['integer'],
    events: {
        'click .o_color_pill': 'clickPill',
    },
    init: function () {
        this.totalColors = 10;
        this._super.apply(this, arguments);
    },

    willStart: function () {
        var self = this;
        this.colorGroupData = {};
        var colorDataPromise = this._rpc({
            model: this.model,
            method: 'read_group',
            domain: [],
            fields: ['color'],
            groupBy: ['color'],
        }).then(function (result) {
            _.each(result, function (r) {
                self.colorGroupData[r.color] = r.color_count;
            });
        });
        return Promise.all([this._super.apply(this, arguments), colorDataPromise]);
    },

    _renderEdit: function () {
        this.$el.empty();
        var pills = qweb.render('FieldColorPills', {widget: this});
        this.$el.append(pills);
        this.$el.find('[data-toggle="tooltip"]').tooltip();
    },

    _renderReadonly: function () {
        var className = "o_color_pill active readonly o_color_" + this.value;
        this.$el.append($('<span>', {
            'class': className,
        }));
    },
    clickPill: function (ev) {
        var $target = $(ev.currentTarget);
        var data = $target.data();
        this._setValue(data.val.toString());
        if (mobile.methods.showToast) {
            mobile.methods.showToast({ 'message': 'Color changed' });
        }
    }

});

fieldRegistry.add('int_color', colorField);

return {
    colorField: colorField,
};
});
