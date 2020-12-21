odoo.define('my.component', function (require) {
    "use strict";

    const { Component, useState } = owl;
    const { xml } = owl.tags;

    class MyComponent extends Component {

        static template = xml`
            <div class="bg-info text-center p-2">
                <i class="fa fa-arrow-left p-1"
                    style="cursor: pointer;"
                    t-on-click="onPrevious"> </i>
                <b t-esc="messageList[Math.abs(state.currentIndex%4)]"/>
                <i class="fa fa-arrow-right p-1"
                    style="cursor: pointer;"
                    t-on-click="onNext"> </i>
                <i class="fa fa-close p-1 float-right"
                    style="cursor: pointer;"
                    t-on-click="onRemove"> </i>
            </div>`

        constructor() {
            console.log('CALLED:> constructor');
            super(...arguments);
            this.messageList = [
                'Hello World',
                'Welcome to Odoo',
                'Odoo is awesome',
                'You are awesome too'
            ];
            this.state = useState({ currentIndex: 0 });
        }

        onRemove(ev) {
            this.destroy();
        }
        onNext(ev) {
            this.state.currentIndex++;
        }
        onPrevious(ev) {
            this.state.currentIndex--;
        }
    }

    owl.utils.whenReady().then(() => {
        const app = new MyComponent();
        app.mount(document.body);
    });

});
