from odoo import api, fields, models

class Pegawai (models.Model):
    _name = 'restaurant.pegawai'
    _description = 'New description'
    
    name = fields.Char(string='Nama')
    alamat = fields.Char(string='Alamat')
    gaji = fields.Integer(string='Gaji')
    no_hp = fields.Char(string='No Handphone')
    jabatan = fields.Char(string='Jabatan')
    
    status = fields.Selection([
        ('menikah', 'Menikah'), ('belum menikah', 'Belum menikah')
    ], string='Status', required='True')
    
    gender = fields.Selection([
        ('male', 'Male'), ('female', 'Female')
    ], string='Gender', required='True')
    
    
    
    
    
    
    

    
    
    
    