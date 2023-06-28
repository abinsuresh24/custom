from odoo import models, fields


class ModelTest(models.Model):
    _name = "model.test"
    _description = "description"

    name = fields.Char(string='Name', help='Name', required=True)
    roll_no = fields.Integer(string='Roll no', help='roll no')
    float = fields.Float(string='Float', help='float')
    document = fields.Binary(string='Document', help='document')
    Image = fields.Image(string='Image', help='image')
    dob = fields.Date(string='DOB', help='dob')
    true = fields.Boolean(string='demo')
    date_time = fields.Datetime()
    state = fields.Selection([('kerala', 'kerala'), ('others', 'others')], string='state', help='state')
    description = fields.Text(string="description")
    # product_id = fields.Many2one('product.product')
    # product_ids = fields.Many2many('product.product')
    # others_ids = fields.One2many()
    # price = fields.Monetary()
    # currency_id = fields.Many2one("res.currency")
