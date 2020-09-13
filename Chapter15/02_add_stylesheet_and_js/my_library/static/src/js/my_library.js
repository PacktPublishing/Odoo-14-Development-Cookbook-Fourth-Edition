odoo.define('my_library', function (require) {
    var core = require('web.core');

    alert(core._t('Hello world'));
    return {
        // if you created functionality to export, add it here
    }
});
