# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions
from odoo.exceptions import ValidationError


# class our_course(models.Model):
#     _name = 'our_course.our_course'
#     _description = 'our_course.our_course'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

class Team(models.Model):
    _name = 'our_course.team'
    _description = 'Team'
    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    position = fields.Char(string='Position')
    created_date = fields.Date(string='Created Date', default=fields.Date.today)
    updated_date = fields.Datetime(string='Updated Date', default=fields.Datetime.now)
    status = fields.Boolean(string='Status', default=True)


class Course(models.Model):
    _name = 'our_course.course'
    _description = 'Course'
    name = fields.Char(string='Course Name', required=True)
    image = fields.Binary(string='Image')
    description = fields.Text(string='Description')
    teacher = fields.Many2one('our_course.team', string='Teacher')
    status = fields.Boolean(string='Status', default=True)
    created_date = fields.Date(string='Created Date', default=fields.Date.today)
    updated_date = fields.Datetime(string='Updated Date', default=fields.Datetime.now)


# F.A.Q
class FAQ(models.Model):
    _name = 'our_course.faq'
    _description = 'FAQ'
    question = fields.Char(string='Question', required=True)
    answer = fields.Text(string='Answer')
    status = fields.Boolean(string='Status', default=True)
    created_date = fields.Date(string='Created Date', default=fields.Date.today)
    updated_date = fields.Datetime(string='Updated Date', default=fields.Datetime.now)


# Reviews
class Reviews(models.Model):
    _name = 'our_course.review'
    _description = 'Reviews'
    image = fields.Binary(string='Image')
    name = fields.Char(string='Name', required=True)
    stars = fields.Selection([
        ('1', '1 Star'),
        ('2', '2 Stars'),
        ('3', '3 Stars'),
        ('4', '4 Stars'),
        ('5', '5 Stars'),
    ], string='Stars', required=True)
    review = fields.Text(string='Review')
    status = fields.Boolean(string='Status', default=True)
    created_date = fields.Date(string='Created Date', default=fields.Date.today)
    updated_date = fields.Datetime(string='Updated Date', default=fields.Datetime.now)
