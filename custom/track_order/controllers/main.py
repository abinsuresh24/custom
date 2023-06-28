# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
from odoo.addons.portal.controllers.portal import CustomerPortal


class Orders(CustomerPortal):
    """Class defined for getting details of transfers from the backend and
    inherited for customize customer portal in the website"""

    def _prepare_home_portal_values(self, counters):
        """Inherited function for adding track orders in the portal"""
        val = super(Orders, self)._prepare_home_portal_values(counters)
        val['order_count'] = request.env['stock.picking'].sudo().search_count(
            [])
        return val

    @http.route('/my/track_order_web', type='http', auth='public', website=True)
    def track_order_web(self, search="", search_in="All"):
        """Function defined for getting transfer details from stock_picking
        and pass it to the front end"""
        search_list = {
            'All': {'label': 'All', 'input': 'All',
                    'domain': [('name', 'ilike', search)]},
        }
        search_domain = search_list[search_in]['domain']
        order = request.env['stock.picking'].sudo().search(search_domain, [])
        return request.render("track_order.track_order_portal_list",
                              {'order': order,
                               'search': search,
                               'searchbar_inputs': search_list,
                               'search_in': search_in})
