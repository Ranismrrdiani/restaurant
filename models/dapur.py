from odoo import api, fields, models

class Dapur (models.Model):
    _name = 'restaurant.dapur'
    _description = 'New description'
    _rec_name = 'alat_dapur'
    
    alat_dapur = fields.Char(string='Alat Dapur')
    img = fields.Binary(string='Image')
    bahan_makanan = fields.Char(string='Bahan Makanan')
    makanan_ids = fields.One2many(comodel_name='restaurant.makanan', 
                                  inverse_name='dapur_id', 
                                  string='Makanannya')
    
    
    