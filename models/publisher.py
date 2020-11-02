# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Publisher(models.Model):
    _name = 'library.publisher'
    _description = 'library_publisher'


    name = fields.Char(string='Publisher', required=True)