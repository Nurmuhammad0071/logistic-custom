# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


# class OurProducts(http.Controller):
#     @http.route('/our_course/our_course', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/our_course/our_course/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('our_course.listing', {
#             'root': '/our_course/our_course',
#             'objects': http.request.env['our_course.our_course'].search([]),
#         })

#     @http.route('/our_course/our_course/objects/<model("our_course.our_course"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('our_course.object', {
#             'object': obj
#         })

class OurCourse(http.Controller):
    @http.route('/', auth='public', website=True)
    def display_services(self, **kw):
        service_model = http.request.env['our_course.course']
        team_model = http.request.env['our_course.team']
        faq_model = http.request.env['our_course.faq']
        reviews_model = http.request.env['our_course.review']

        services = service_model.search([
            ('status', '=', True)
        ])
        teams = team_model.search([
            ('status', '=', True)
        ])
        faqs = faq_model.search([
            ('status', '=', True)
        ])
        reviews = reviews_model.search([
            ('status', '=', True)

        ])

        return http.request.render('website.homepage', {
            'our_course': services,
            'our_team': teams,
            'our_faq': faqs,
            'our_reviews': reviews

        })
