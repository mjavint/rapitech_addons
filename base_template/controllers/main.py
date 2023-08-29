# -*- coding: utf-8 -*-
# from odoo import http


# class Addons/baseTemplate(http.Controller):
#     @http.route('/addons/base_template/addons/base_template', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/addons/base_template/addons/base_template/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('addons/base_template.listing', {
#             'root': '/addons/base_template/addons/base_template',
#             'objects': http.request.env['addons/base_template.addons/base_template'].search([]),
#         })

#     @http.route('/addons/base_template/addons/base_template/objects/<model("addons/base_template.addons/base_template"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('addons/base_template.object', {
#             'object': obj
#         })
