/** @odoo-module **/

    import { Orderline } from 'point_of_sale.models';
    import Registries from 'point_of_sale.Registries';
    var core = require('web.core');
    const _t = core._t;
    const { Gui } = require('point_of_sale.Gui');
    const Discount = (Orderline) => class Discount extends Orderline{
    set_discount(discount){
    super.set_discount(...arguments);
    console.log(discount);
    var pos_disc=this.pos.config.max_discount;
    console.warn(pos_disc);
    var pos_categ=this.pos.config.categ_ids[0];
    console.warn(pos_categ);
    console.warn(this.pos);
    var categ= this.get_product().pos_categ_id[0];
    console.log(categ);
//    var pos_categ = this.pos.res_config_settings[4]['pos_categ_ids'][0];
//    console.log(pos_categ);
//    var max= this.pos.res_config_settings[4]['pos_max_discount'];
    if(pos_categ == categ){
        if(discount > pos_disc){
            Gui.showPopup("ErrorPopup", {
                                'title': _t("Discount Not Possible"),
                                'body':  _t("You cannot apply discount above the discount limit."),
                            });
        }
    }
    var max= this.pos.config.pos_max_discount;

    console.warn(max);
    }
    }
    Registries.Model.extend(Orderline, Discount);
