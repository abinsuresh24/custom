/** @odoo-module **/

import { Orderline } from 'point_of_sale.models';
import Registries from 'point_of_sale.Registries';
const CustomerOrderLine = (Orderline) => class CustomerOrderLine extends Orderline{
    export_for_printing(){
        let result = super.export_for_printing(...arguments);
        result.owner_id = this.get_product().owner_id;
        return result;
    }
}
Registries.Model.extend(Orderline,CustomerOrderLine);
