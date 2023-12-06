from charset_normalizer import models


class sale(models.Model):
    _name = 'student.certificate'
    _inherit = 'sale.order'
    _description = 'student sale verification'
