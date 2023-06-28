odoo.define('website_snippet.snippet', function(require) {
    'use strict';
    var PublicWidget = require('web.public.widget');
    var rpc = require('web.rpc');
    var core = require('web.core');
    var qweb = core.qweb;
    var Dynamic = PublicWidget.Widget.extend({
        selector: '.event',willStart: async function() {
            var self = this;
            await rpc.query({route: '/latest_events',}).then((data) => {
            this.data = data;
            });
        },
        start: function() {
        var chunks = _.chunk(this.data, 4)
        chunks[0].is_active = true
        this.$el.find('#courosel').html(qweb.render('event', {chunks}))
        },
    });
    PublicWidget.registry.event = Dynamic;
    return Dynamic;
});