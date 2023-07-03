/** @odoo-module **/

import PaymentScreen from 'point_of_sale.PaymentScreen';
import Registries from 'point_of_sale.Registries';
var core = require('web.core');
var _t = core._t;

const PurchaseLimit = (PaymentScreen) => class PurchaseLimit extends
PaymentScreen {
    //Inhering the PaymentScreen for adding new functions
    async validateOrder() {
        //Function defined for checking customer and purchase limit
        //for the customer when validating the order
        var order = this.env.pos.get_order();
        var sub_total = order.get_subtotal();
        var partner = this.env.pos.get_order().get_partner();
        if (!partner) {
            const { confirmed } = this.showPopup('ConfirmPopup', {
                title: this.env._t('Customer Needed'),
                body: this.env._t('Please select a customer'),
            });
        }
        else {
            var purchase_amount = partner.purchase_amount;
            var purchase_limit = partner.purchase_limit;
            if (purchase_limit) {
                if (sub_total > purchase_amount) {
                    const { confirmed, payload } = this.showPopup
                    ('ConfirmPopup', {
                        title: this.env._t('Purchase Limit'),
                        body: _.str.sprintf(this.env._t
                        ('Purchase limit %s exceeded'), partner.purchase_amount)
                    });
                }
                else{
                await super.validateOrder();
                }
            }
            else {
                await super.validateOrder();
            }
        }
    }
}
Registries.Component.extend(PaymentScreen, PurchaseLimit);
