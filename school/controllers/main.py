# -*- coding: utf-8 -*-
# from odoo import http


# class Addons/school(http.Controller):
#     @http.route('/addons/school/addons/school', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/addons/school/addons/school/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('addons/school.listing', {
#             'root': '/addons/school/addons/school',
#             'objects': http.request.env['addons/school.addons/school'].search([]),
#         })

#     @http.route('/addons/school/addons/school/objects/<model("addons/school.addons/school"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('addons/school.object', {
#             'object': obj
#         })
