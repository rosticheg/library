# -*- coding: utf-8 -*-
from odoo import http

# class C:\odoo\library(http.Controller):
#     @http.route('/c:\odoo\library/c:\odoo\library/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/c:\odoo\library/c:\odoo\library/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('c:\odoo\library.listing', {
#             'root': '/c:\odoo\library/c:\odoo\library',
#             'objects': http.request.env['c:\odoo\library.c:\odoo\library'].search([]),
#         })

#     @http.route('/c:\odoo\library/c:\odoo\library/objects/<model("c:\odoo\library.c:\odoo\library"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('c:\odoo\library.object', {
#             'object': obj
#         })