odoo.define('my.component', function (require) {
    "use strict";

    const { Component } = owl;
    const { xml } = owl.tags;

    class MyComponent extends Component {
        static template = xml`
            <div class="bg-info text-center p-2">
                <b> Welcome to Odoo </b>
                <i class="fa fa-close p-1 float-right"
                    style="cursor: pointer;"
                    t-on-click="onRemove"> </i>
            </div>`
        onRemove(ev) {
            this.destroy();
        }
    }

    owl.utils.whenReady().then(() => {
        const app = new MyComponent();
        app.mount(document.body);
    });

});
