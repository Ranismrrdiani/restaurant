import string
from odoo import api, fields, models

class Makanan (models.Model):
    _name = 'restaurant.makanan'
    _description = 'New description'
    
    name = fields.Char (string = 'Nama Menu')
    deskripsi = fields.Char (string = 'Deskripsi')
    
    jenis = fields.Selection([('drinks', 'Drinks'), 
                              ('dessert', 'Dessert'), 
                              ('appetizer', 'Appetizer'),
                              ('main course', 'Main Course')],
                             string='Jenis')
    
    harga = fields.Integer(string='Harga')
    stok = fields.Integer(string='Stok')
    img = fields.Binary(string='Image')
    
    pesanan_id = fields.Many2one(comodel_name='restaurant.pesan', string='Pesanan')
    
    dapur_id = fields.Many2one(comodel_name='restaurant.dapur', string='Alat Dapur')
    pelanggan_id = fields. Many2one(comodel_name='restaurant.pelanggan', string='Pelanggan')
    
    
    
    
    
    
    