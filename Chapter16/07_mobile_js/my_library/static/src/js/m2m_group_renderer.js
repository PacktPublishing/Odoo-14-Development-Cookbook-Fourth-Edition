odoo.define('m2m_group.Renderer', function (require) {
    'use strict';

    var AbstractRenderer = require('web.AbstractRenderer');
    var core = require('web.core');

    var qweb = core.qweb;

    var M2mGroupRenderer = AbstractRenderer.extend({
        events: _.extend({}, AbstractRenderer.prototype.events, {
            'click .o_primay_button': '_onClickButton',
        }),
        _render: function () {
            var self = this;
            this.$el.empty();
            this.$el.append(qweb.render('ViewM2mGroup', {
                'groups': this.state,
            }));
            return this._super.apply(this, arguments);
        },
        _onClickButton: function (ev) {
            ev.preventDefault();
            var target =  $(ev.currentTarget);
            var group_id = target.data('group');
            var children_ids = _.map(this.state[group_id].children, function (group_id) {
                return group_id.id;
            });
            this.trigger_up('btn_clicked', {
                'domain': [['id', 'in', children_ids]]
            });
        }
    });

    return M2mGroupRenderer;

});
