odoo.define('m2m_group.Controller', function (require) {
    'use strict';

    var AbstractController = require('web.AbstractController');
    var core = require('web.core');
    var qweb = core.qweb;

    var M2mGroupController = AbstractController.extend({
        custom_events: _.extend({}, AbstractController.prototype.custom_events, {
            'btn_clicked': '_onBtnClicked',
        }),
        renderButtons: function ($node) {
            if ($node) {
                this.$buttons = $(qweb.render('ViewM2mGroup.buttons'));
                this.$buttons.appendTo($node);
                this.$buttons.on('click', 'button', this._onAddButtonClick.bind(this));
            }
        },
        _onBtnClicked: function (ev) {
            this.do_action({
                type: 'ir.actions.act_window',
                name: this.title,
                res_model: this.modelName,
                views: [[false, 'list'], [false, 'form']],
                domain: ev.data.domain,
            });
        },
        _onAddButtonClick: function (ev) {
            this.do_action({
                type: 'ir.actions.act_window',
                name: this.title,
                res_model: this.modelName,
                views: [[false, 'form']],
                target: 'new'
            });
        },


    });

    return M2mGroupController;

});
