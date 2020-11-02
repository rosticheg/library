# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Rental(models.Model):
    _name = 'library.rental'
    _description = 'library_rental'


    customer_id = fields.Many2one('library.partner')
    book_id = fields.Many2one('library.book')
    rental_date = fields.Date("Rental Date", default=fields.Date)
    return_date = fields.Date("Return Date", default=fields.Date)