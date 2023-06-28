# -*- coding: utf-8 -*-
import json
from odoo import http
from odoo.http import request


class Sales(http.Controller):
    """Class defined for adding events to the snippet"""
    @http.route(['/latest_events'], type="json", auth="public")
    def latest_events(self):
        """Function defined for finding the latest four events"""
        events = request.env['event.event'].sudo().search_read([], limit=4,
                                                        order='date_begin desc')
        return events
