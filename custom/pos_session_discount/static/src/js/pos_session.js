/** @odoo-module **/

import { PosGlobalState} from 'point_of_sale.models';
import Registries from 'point_of_sale.Registries';
const NewPosGlobalState = (PosGlobalState) => class NewPosGlobalState extends PosGlobalState {
   async _processData(loadedData) {

 await super._processData(...arguments);

 this.discount_category = loadedData['discount.category'];

 }
}
Registries.Model.extend(PosGlobalState, NewPosGlobalState);