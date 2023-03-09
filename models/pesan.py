from odoo import api, fields, models

class Pesan (models.Model):
    _name = 'restaurant.pesan'
    _description = 'New description'
    
    name = fields.Char(string='Nama')
    
    pesandetail_ids = fields.One2many(comodel_name='restaurant.pesandetail', 
                                      inverse_name='pesan_id', 
                                      string='Pesanan')
    
    pegawai_id = fields.Many2one(comodel_name='restaurant.pegawai', string='Pegawai')
    
    pelanggan_id = fields.Many2one(comodel_name='restaurant.pelanggan', string='Pelanggan')
    
    tanggal = fields.Datetime(string='Tanggal Pesan',default=fields.Datetime.now)
    no_meja = fields.Char(string='Nomor Meja')
    
    metode = fields.Selection([
        ('cash', 'Cash'), 
        ('e-wallet', 'E-Wallet'), 
        ('dompet digital', 'Dompet Digital'), 
        ('qris', 'QRIS')
    ], string='Metode Pembayaran', required='True')
    
    makanan_ids = fields.One2many(comodel_name='restaurant.makanan', 
                                  inverse_name='pesanan_id',
                                  string='Makanannya')
    
    total_harga = fields.Integer(compute='_compute_total_harga',string='Total Harga',store=True)
     
    @api.depends('makanan_ids')
    def _compute_total_harga(self):
        for record in self:
            a = sum(self.env['restaurant.makanan'].search([('pesanan_id', '=', record.id)]).mapped('harga'))
            b = sum(self.env['restaurant.pesandetail'].search([('pesan_id', '=', record.id)]).mapped('harga'))
            record.total_harga = a + b
            
    sudah_bayar = fields.Boolean(string='Sudah Bayar', default=False)        

class PesanDetail(models.Model):
    _name = 'restaurant.pesandetail'
    _description = 'New Description'

    pesan_id = fields.Many2one(comodel_name='restaurant.pesan', string='Pesanan')
    makanan_id = fields.Many2one(comodel_name='restaurant.makanan', string='Makanannya')
    
    name = fields.Char(string='Name')
    harga = fields.Integer(compute='_compute_harga', string='total harga')
    harga_satuan = fields.Integer(compute='_compute_harga_satuan', string='harga_satuan')
    
    @api.depends('makanan_id')
    def _compute_harga_satuan(self):
        for record in self:
            record.harga_satuan = record.makanan_id.harga
    
    qty = fields.Integer(string='Quantity')
    
    @api.depends('qty','harga_satuan')
    def _compute_harga(self):
        for record in self:
           record.harga = record.harga_satuan * record.qty
           
    @api.model
    def create(self,vals):
        record = super(PesanDetail, self).create(vals) 
        if record.qty:
            self.env['restaurant.makanan'].search([('id','=',record.makanan_id.id)]).write({'stok':record.makanan_id.stok-record.qty})
            return record
    
    
    