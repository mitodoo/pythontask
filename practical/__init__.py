from odoo import models, fields,

class sale(models.Model):
    _name = 'student.certificate'
    _inherit = 'sale.order'
    _description = 'student sale verification'