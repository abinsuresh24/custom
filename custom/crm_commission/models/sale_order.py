# -*- coding: utf-8 -*-
from odoo import api, fields, models


class SaleOrder(models.Model):
    """class defined for adding commission in the sales sale order"""

    _inherit = 'sale.order'

    category = fields.Selection(
        [('stc', 'STC'), ('etc', 'ETC'), ('ptc', 'PTC')])

    commission_product_id = fields.Many2one('commission.product')
    commission_amount = fields.Float(string="Commission amount")
    commission_plan_id = fields.Many2one('crm.commission',
                                         string="Commission Plan",
                                         compute="_compute_plan",
                                         readonly=False)

    @api.depends('user_id')
    def _compute_plan(self):
        """Function added for getting commission plans in the sale order"""
        self.commission_plan_id = self.user_id.salesperson_commission_id

    @api.onchange('order_line')
    def _onchange_commission_plan(self):
        """Function defined for adding commission plan
        based on the order line in the sale order"""
        self.commission_amount = 0
        graduation1 = 0
        graduation2 = 0
        prev_amount = 0
        if self.commission_plan_id.plan_type == 'product_wise':
            for product in self.commission_plan_id.commission_product_ids:
                for line in self.order_line:
                    if product.product_id.id == line.product_template_id.id:
                        commission = line.price_subtotal * product.rate / 100
                        if commission > product.max_commission:
                            commission = product.max_commission
                        self.commission_amount = self.commission_amount \
                                                 + commission
        else:
            if self.commission_plan_id.revenue_type == 'straight':
                self.commission_amount = self.amount_total \
                                         * self.commission_plan_id.straight_rate \
                                         / 100
            else:
                for revenue in self.commission_plan_id.commission_revenue_ids:
                    if self.amount_total > revenue.from_amount:
                        if self.amount_total > revenue.to_amount:
                            prev_amount = revenue.to_amount
                            graduation1 = graduation1 + (
                                    revenue.to_amount
                                    - revenue.from_amount) * revenue.rate / 100
                        else:
                            graduation2 = graduation2 + (
                                    self.amount_total - prev_amount) \
                                          * revenue.rate / 100
                        new_commission = graduation1 + graduation2
                        self.commission_amount = new_commission

    def action_confirm(self):
        """Function defined for adding commission details in
        the commission menu in sale order"""
        res = super(SaleOrder, self).action_confirm()
        self.env['sales.commission'].create({
            'reference_id': self.id,
            'partner_id': self.partner_id.id,
            'commission_amount': self.commission_amount,
            'commission_plan_id': self.commission_plan_id.id})
        return res

    def order_commission(self):
        """Function defined for smart button to show commission details"""
        return {
            'type': 'ir.actions.act_window',
            'name': 'sales commissions',
            'view_mode': 'tree,form',
            'res_model': 'sale.order',
            'domain': [('id', '=', self.id)],
            'context': {'create': False}
        }
class SaleOrderLine(models.Model):
    """class defined for adding milestone in the sale order"""
    _inherit = 'sale.order.line'

    category1 = fields.Selection(
        [('stc', 'STC'), ('etc', 'ETC'), ('ptc', 'PTC')])
    stc = fields.Float(String="STC")
    etc = fields.Float(String="ETC")
    ptc = fields.Float(String="PTC")
