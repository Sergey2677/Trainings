# -*- coding: utf-8 -*-
# from odoo import http


# class OdooSergey(http.Controller):
#     @http.route('/odoo_sergey/odoo_sergey', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo_sergey/odoo_sergey/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo_sergey.listing', {
#             'root': '/odoo_sergey/odoo_sergey',
#             'objects': http.request.env['odoo_sergey.odoo_sergey'].search([]),
#         })

#     @http.route('/odoo_sergey/odoo_sergey/objects/<model("odoo_sergey.odoo_sergey"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo_sergey.object', {
#             'object': obj
#         })
