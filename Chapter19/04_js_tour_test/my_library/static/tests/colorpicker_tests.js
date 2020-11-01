odoo.define('colorpicker_tests', function (require) {
"use strict";

var FormView = require('web.FormView');
var testUtils = require('web.test_utils');

var testUtilsDom = require('web.test_utils_dom');

function clickCreate(kanban) {
    return testUtilsDom.click(kanban.$buttons.find('.o-kanban-button-new'));
}

QUnit.module('Color Picker Tests', {
    beforeEach: function () {
        this.data = {
            book: {
                fields: {
                    name: { string: "Name", type: "char" },
                    color: { string: "color", type: "integer"},
                },
                records: [{
                    id: 1,
                    name: "Book 1",
                    color: 1
                }, {
                    id: 2,
                    name: "Book 2",
                    color: 3
                }]
            }
        };
    }
    }, function () {

    QUnit.only('int_color field test cases', async function (assert) {
        assert.expect(2);

        var form = await testUtils.createView({
            View: FormView,
            model: 'book',
            data: this.data,
            arch: '<form string="Books">' +
                '<group>' +
                    '<field name="name"/>' +
                    '<field name="color" widget="int_color"/>' +
                '</group>' +
                '</form>',
            res_id: 1,
        });

        await testUtils.form.clickEdit(form);

        assert.strictEqual(form.$('.o_int_colorpicker .o_color_pill').length, 10,
            "colorpicker should have 10 pills");

        await testUtils.dom.click(form.$('.o_int_colorpicker .o_color_pill:eq(5)'));

        assert.strictEqual(form.$('.o_int_colorpicker .o_color_5').hasClass('active'), true,
            "click on pill should make pill active");

        form.destroy();
    });
});

});
