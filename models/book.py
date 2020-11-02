# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Book(models.Model):
    _name = 'library.book'
    _description = 'library_book'


    name = fields.Char(string='Book', required=True)
    author_ids = fields.Many2many("library.partner", string="Author IDS")
    edition_date = fields.Date("Edition Date", default=fields.Date)
    isbn = fields.Char(string='ISBN')
    publisher_id = fields.Many2one('library.publisher')
    rental_ids = fields.One2many('library.rental', string="Rental IDS")