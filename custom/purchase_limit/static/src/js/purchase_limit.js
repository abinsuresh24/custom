odoo.define('purchase_limit.PaymentScreen', function(require) {
    'use strict';

    const PaymentScreen = require('point_of_sale.PaymentScreen');
    const Registries = require('point_of_sale.Registries');
     var core = require('web.core');
     var _t= core._t;

    const PurchaseLimit = (PaymentScreen) => class PurchaseLimit extends PaymentScreen{
    setup(){
    super.setup()
    console.log("111")}
//    super._onClickPay()
    _onClickPay(){
    var self =this;
    var order= self.pos.get_order();
    var sub_total=order.get_subtotal();
    purchase_amount = this.get_partner().purchase_amount;
    if(sub_total > purchase_amount){
    const { confirmed, payload } = this.showPopup('ErrorTracebackPopup', {
       title: this.env._t('Purchase Limit'),
       body: this.env._t('Purchase limit exceeded'),
   });
   if (confirmed) {
       console.log(payload, 'payload')
   }
    }
    console.warn(sub_total);
    console.warn('111111111111111111111111111');
    }
    }
    Registries.Component.extend(PaymentScreen, PurchaseLimit);
    return PaymentScreen;
});







//-------------------------------------------------------------------------
//    purchase_amount = this.get_partner().purchase_amount;
//    if(sub_total > purchase_amount){
//    const { confirmed, payload } = await this.showPopup('ErrorTracebackPopup', {
//       title: this.env._t('Purchase Limit'),
//       body: this.env._t('Purchase limit exceeded'),
//   });
//   if (confirmed) {
//       console.log(payload, 'payload')
//   }
//    }
//-------------------------------------
//odoo.define('purchase_limit.PaymentScreen', function (require) {
//    'use strict';
//
//    var Screens= require('point_of_sale.screens');
//    var core = require.('web.core');
//     var _t= core._t;
//
//     Screens.ActionpadWidget.include({
//
//        const PosComponent = require('point_of_sale.PosComponent');
//        const Registries = require('point_of_sale.Registries');
//
//        const PurchaseLimit = (PaymentScreen) => class PurchaseLimit extends PaymentScreen{
//        _onClickPay(){
//        var self =this;
//        this._super();
//        var order= self.pos.get_order();
//        var sub_total=order.get_subtotal();
//        console.warn(sub_total);
//        }var _t= core._t;
//    }
//    Registries.Component.extend(PaymentScreen, PurchaseLimit);
//});