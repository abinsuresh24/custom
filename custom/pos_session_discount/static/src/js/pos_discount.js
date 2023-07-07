/** @odoo-module **/

import { Orderline } from 'point_of_sale.models';
import Registries from 'point_of_sale.Registries';
import core from 'web.core';
const _t = core._t;
import { Gui } from 'point_of_sale.Gui';
const Discount = (Orderline) => class Discount extends Orderline {
    //Inhering the Orderline for adding new functions
  async set_discount(discount) {
    //  Function extended for adding discount limit for selected categories
    super.set_discount(...arguments);
    var pos_disc = this.pos.config.max_discount;
    var pos_categ = this.pos.config.categ_ids;
    var categ = this.product.pos_categ_id[0];
    var order = this.order.orderlines;
    var total_disc = {};
    for (var rec of order) {
      var line_categ = rec.product.pos_categ_id[0];
      if (pos_categ.includes(line_categ)) {
        if (!total_disc[line_categ]) {
          total_disc[line_categ] = 0;
        }
        total_disc[line_categ] += rec.discount;
      }
    }
    for (var category in total_disc) {
      if (total_disc[category] > pos_disc) {
        const { confirmed } = await Gui.showPopup("ConfirmPopup", {
          'title': _t("Discount Not Possible"),
          'body': _.str.sprintf(_t("You cannot apply a discount above the limit of %s percentage"), pos_disc)
        });
        if (confirmed) {
          this.discount = 0;
          this.discountStr = 0;
        }
        if (!confirmed) {
          this.discount = 0;
          this.discountStr = 0;
        }
      }
    }
  }
}
Registries.Model.extend(Orderline, Discount);
