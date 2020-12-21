odoo.define('my_library.tour', function (require) {
"use strict";


var core = require('web.core');
var tour = require('web_tour.tour');

var _t = core._t;

tour.register('library_tour', {
    url: "/web",
    rainbowManMessage: _t("Congrats, you have listed a book."),
    sequence: 5,
    }, [tour.stepUtils.showAppsMenuItem(), {
        trigger: '.o_app[data-menu-xmlid="my_library.library_base_menu"]',
        content: _t('Manage books and authors in <b>Library app</b>.'),
        position: 'right'
    }, {
        trigger: '.o_list_button_add',
        content: _t("Let's create new book."),
        position: 'bottom'
    }, {
        trigger: 'input[name="name"]',
        extra_trigger: '.o_form_editable',
        content: _t('Set the book title'),
        position: 'right',
    }, {
        trigger: '.o_form_button_save',
        content: _t('Save this book record'),
        position: 'bottom',
    }
]);

});
