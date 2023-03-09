from odoo import api, fields, models

class Pelanggan (models.Model):
    _name = 'restaurant.pelanggan'
    _description = 'New description'
    
    name = fields.Char(string='Nama')
    membership = fields.Boolean(string='Apakah member')
    id_pelanggan = fields.Char(string='Id Pelanggan')
    no_hp = fields.Char(string='No Handphone')
    alamat = fields.Char(string='Alamat')
    
    gender = fields.Selection([
        ('male', 'Male'), ('female', 'Female')
    ], string='Gender', required='True')
    
    level = fields.Selection(
        string='Level',
        selection=[('silver', 'Silver'),
                   ('gold', 'Gold'),
                   ('platinum', 'Platinum'),
                   ],
        required=True)
    
    
    
    
    