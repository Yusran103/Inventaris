from django.db import models
from hashid_field import HashidAutoField

# Create your models here.

class Jenis_brg(models.Model):
    """docstring for jenis"""
    id_jenis = models.AutoField(primary_key=True)
    nama_jenis = models.CharField(max_length=100)

    class Meta:
        db_table = "tb_jenis_brg"

    def __str__(self):
        return self.nama_jenis

class Supplier(models.Model):
    id_supplier = models.AutoField(primary_key=True)
    nama_supplier = models.CharField(max_length=100)
    alamat_supplier = models.CharField(max_length=100)
    notlp_supplier = models.CharField(max_length=100)
    class Meta:
        db_table = "tb_supplier"
    
    def __str__(self):
        return self.nama_supplier

class Customer(models.Model):
    id_customer = models.AutoField(primary_key=True)
    nama_customer = models.CharField(max_length=100)
    alamat_customer = models.CharField(max_length=100)
    notlp_customer= models.CharField(max_length=100)
    
    class Meta:
        db_table = "tb_customer"
    
    def __str__(self):
        return self.nama_customer

class Merk_brg(models.Model):
    """docstring for merk"""
    id_merk = models.AutoField(primary_key=True)
    nama_merk = models.CharField(max_length=100)
    class Meta:
        db_table = "tb_merk_brg"
    
    def __str__(self):
        return self.nama_merk

class Tipe_brg(models.Model):
    """docstring for jenis"""
    id_tipe = models.AutoField(primary_key=True)
    nama_tipe = models.CharField(max_length=100)

    class Meta:
        db_table = "tb_tipe_brg"
    
    def __str__(self):
        return self.nama_tipe

class Barang_masuk(models.Model):
    """docstring for barang_masuk"""
    id_brg_masuk = models.AutoField(primary_key=True)
    kd_barang = models.CharField(max_length=10)
    nm_barang = models.CharField(max_length=100)
    sn_barang = models.CharField(max_length=20)
    tgl_masuk = models.DateField()
    jml_masuk = models.IntegerField()
    harga_satuan = models.IntegerField()
    no_resi = models.CharField(max_length=100,blank=True)
    foto_masuk = models.ImageField(upload_to='foto/',blank=True) 
    
    supplier_id = models.ForeignKey(Supplier,on_delete=models.CASCADE,db_column='supplier_id')
    jenis_id = models.ForeignKey(Jenis_brg,on_delete=models.CASCADE,db_column='jenis_id')
    merk_id = models.ForeignKey(Merk_brg,on_delete=models.CASCADE,db_column='merk_id')
    tipe_id = models.ForeignKey(Tipe_brg,on_delete=models.CASCADE,db_column='tipe_id')
    

    class Meta:
        db_table = "tb_barang_masuk"
    
    def __str__(self):
        return self.nm_barang

# barang keluar
class Barangkeluar(models.Model):
    """docstring for barang_keluar"""
    id = models.AutoField(primary_key=True)
    nama_barang = models.CharField(max_length=100)
    tanggal = models.DateField()
    serialnumber = models.CharField(max_length=20)
    kode_barang = models.CharField(max_length=10)
    no_bukti = models.CharField(max_length=20)
    no_resi = models.CharField(max_length=20,blank=True)
    jumlah = models.IntegerField()
    harga_satuan = models.IntegerField()
    total_bayar = models.IntegerField()

    alamat_customer = models.CharField(max_length=100)
    customer_id = models.ForeignKey(Customer, on_delete=models.DO_NOTHING,db_column='customer_id')
    foto_keluar = models.ImageField(upload_to='foto/', blank=True, null=True)

    class Meta:
        db_table = "tb_barang_keluar"

    def __str__(self):
        return self.nama_barang

    # agar file yang diupload bisa dihapus dr folder
    def delete(self, *args, **kwargs):
        self.foto_keluar.delete()
        super().delete(*args, **kwargs)

class Stok_barang(models.Model):
    id_stok = models.AutoField(primary_key=True)
    tanggal = models.DateField()
    nm_barang= models.CharField(max_length=100)
    kd_barang = models.CharField(max_length=100)
    hrg_barang = models.IntegerField()
    jumlah_stok = models.IntegerField(default=0)
    stok_akhir = models.IntegerField(default=0)
    keterangan = models.CharField(max_length=100)
    foto_stok = models.ImageField(upload_to='foto/',blank=True , null=True)
    sn_barang = models.CharField(max_length=20) 

    jenis_id = models.ForeignKey(Jenis_brg, on_delete=models.DO_NOTHING,db_column='jenis_id')
    merk_id = models.ForeignKey(Merk_brg, on_delete=models.DO_NOTHING,db_column='merk_id')
    tipe_id = models.ForeignKey(Tipe_brg, on_delete=models.DO_NOTHING,db_column='tipe_id')

    class Meta:
        db_table = "tb_stok"
    
    def __str__(self):
        return self.kd_barang

class User(models.Model):
    """docstring for user"""
    USER_CHOICES = [
        ('Admin', 'Admin'),
        ('SuperAdmin', 'SuperAdmin'),
    ]

    id_user = models.AutoField(primary_key=True)
    nm_lengkap = models.CharField(max_length=25)
    username = models.CharField(max_length=8)
    password = models.CharField(max_length=8)
    level = models.CharField(
        max_length=9, choices=USER_CHOICES, default='Admin')

    class Meta:
        db_table = "tb_user"
    
    def __str__(self):
        return self.nm_lengkap

