from odoo import fields, models


class LibraryBookCategory(models.Model):
    _name = 'library.book.category'
    _description = "Library Book's Category"

    name = fields.Char()
