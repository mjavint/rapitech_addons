# -*- coding: utf-8 -*-
from odoo import http


class SchoolController(http.Controller):
    @http.route('/school', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/school/objects', auth='public')
    def list(self, **kw):
        return http.request.render(
            'school.listing',
            {
                'root': 'school',
                'objects': http.request.env['school'].search([]),
            },
        )

    @http.route('/school/objects/<model("school"):obj>', auth='public')
    def object(self, obj, **kw):
        return http.request.render('school.object', {'object': obj})
