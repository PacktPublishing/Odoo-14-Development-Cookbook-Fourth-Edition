odoo.define('m2m_group.View', function (require) {
    'use strict';

    var AbstractView = require('web.AbstractView');
    var view_registry = require('web.view_registry');
    var M2mGroupController = require('m2m_group.Controller');
    var M2mGroupModel = require('m2m_group.Model');
    var M2mGroupRenderer = require('m2m_group.Renderer');


    var M2mGroupView = AbstractView.extend({
        display_name: 'Author',
        icon: 'fa-id-card-o',
        config: _.extend({}, AbstractView.prototype.config, {
            Model: M2mGroupModel,
            Controller: M2mGroupController,
            Renderer: M2mGroupRenderer,
        }),

        viewType: 'm2m_group',
        searchMenuTypes: ['filter', 'favorite'],
        accesskey: "a",

        init: function (viewInfo, params) {
            this._super.apply(this, arguments);
            var attrs = this.arch.attrs;

            if (!attrs.m2m_field) {
                throw new Error('M2m view has not defined "m2m_field" attribute.');
            }
            // Model Parameters
            this.loadParams.m2m_field = attrs.m2m_field;

        },
    });

    view_registry.add('m2m_group', M2mGroupView);

    return M2mGroupView;

});
