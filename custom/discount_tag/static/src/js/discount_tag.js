/** @odoo-module **/

import { Orderline } from 'point_of_sale.models';
import Registries from 'point_of_sale.Registries';
const CustomerOrderLine = (Orderline) => class CustomerOrderLine extends Orderline{
    export_for_printing(){
        let result = super.export_for_printing(...arguments);
        result.discount_tag = this.get_product().discount_tag;
        return result;
    }
}
Registries.Model.extend(Orderline,CustomerOrderLine);
