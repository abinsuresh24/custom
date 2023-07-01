odoo.define('purchase_limit.PaymentScreen', function(require) {
    'use strict';

    const useState = owl.hooks;
    const AbstractAwaitablePopup = require('point_of_sale.AbstractAwaitablePopup');
    const useAutoFocusToLast = require('point_of_sale.custom_hooks');
    const PaymentScreen = require('point_of_sale.PaymentScreen');
    const Registries = require('point_of_sale.Registries');
    var core = require('web.core');
    var _t= core._t;

    const PurchaseLimit = (PaymentScreen) => class PurchaseLimit extends PaymentScreen{
    validateOrder(){
    super.validateOrder()
    var self =this;
    var order= self.env.pos.get_order();
    var sub_total=order.get_subtotal();
    var partner = this.env.pos.get_order().get_partner();
    var amount= partner.purchase_amount;
    var p_limit=partner.purchase_limit;
    console.log(p_limit);
    if (p_limit){
    if(sub_total>amount){
    const { confirmed, payload } = this.showPopup('ConfirmPopup', {
       title: this.env._t('Purchase Limit'),
       body: _.str.sprintf(this.env._t('Purchase limit %s exceeded'), partner.purchase_amount),
   });
   if (confirmed) {
       console.log(payload, 'payload')
   }
    }
    }
    }
    }
    Registries.Component.extend(PaymentScreen, PurchaseLimit);
    return PaymentScreen;
});
