/** @odoo-module */

const ProductScreen = require('point_of_sale.ProductScreen');
const Registries = require('point_of_sale.Registries');
import core from 'web.core';
const _t = core._t;
import { Gui } from 'point_of_sale.Gui';
const CustomOrder = (ProductScreen) => class CustomOrder extends ProductScreen {
      //      Extending payment button in product screen
      async _onClickPay() {
           //      Function extended for setting discount limit for each category
           const pos_category = this.env.pos.discount_category;
           var orderLines = this.env.pos.get_order().get_orderlines();
           var product=orderLines.product
           var config_categ =this.env.pos.config.disc_category_ids
           let totalDiscount = 0;
           for( var rec of pos_category){
           for (const orderLine of orderLines) {
           for(var category of config_categ){
           if(category == rec['id']){
               if (orderLine.product.pos_categ_id[0] === rec.category_id[0]) {
                   totalDiscount += orderLine.get_discount();
               }
               if(totalDiscount>rec.pos_discount){
               const { confirmed } = await Gui.showPopup("ErrorPopup", {
                    'title': _t("Discount Not Possible"),
                    'body': _t("You cannot apply a discount above the limit of percentage")
               });
               return;
               }
               }

           }
           }
           }
           super._onClickPay();
      }
}
Registries.Component.extend(ProductScreen, CustomOrder);