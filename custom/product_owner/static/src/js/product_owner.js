odoo.define('product_owner.models', function (require) {
"use strict";
	var { Orderline } = require('point_of_sale.models');
	var Registries = require('point_of_sale.Registries');
	const CustomerOrderLine = (Orderline) => class CustomerOrderLine extends Orderline{
	    export_for_printing(){
	        var result = super.export_for_printing(...arguments);
	        result.owner_id = this.get_product().owner_id;
	        return result;
	    }
	}
    Registries.Model.extend(Orderline,CustomerOrderLine);
});
