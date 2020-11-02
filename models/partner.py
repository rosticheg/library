# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Partner(models.Model):
    _name = 'library.partner'
    _description = 'library_partner'


    name = fields.Char(string='Partner', required=True)
    email = fields.Char(string='Email', required=True)
    address = fields.Text(string='Address')
    partner_type = fields.Selection([('customer', 'Customer'), ('author', 'Author'),], default='customer')
    rental_ids = fields.One2many('library.rental')
