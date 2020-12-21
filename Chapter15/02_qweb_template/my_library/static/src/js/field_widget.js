odoo.define('my_field_widget', function (require) {
"use strict";

var AbstractField = require('web.AbstractField');
var fieldRegistry = require('web.field_registry');

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
    _renderEdit: function () {
        this.$el.empty();
        var pills = qweb.render('FieldColorPills', {widget: this});
        this.$el.append(pills);
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
    }

});

fieldRegistry.add('int_color', colorField);

return {
    colorField: colorField,
};
});
