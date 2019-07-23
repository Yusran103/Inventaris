from django.db import models

# Create your models here.

class jenis_brg(models.Model):
    """docstring for jenis"""
    id_jenis = models.AutoField(primary_key=True)
    nama_jenis = models.CharField(max_length=100)

    class Meta:
        db_table = "tb_jenis_brg"

    def __str__(self):
        return self.nama_jenis

class supplier(models.Model):
    id_supplier = models.AutoField(primary_key=True)
    nama_supplier = models.CharField(max_length=100)
    alamat_supplier = models.CharField(max_length=100)
    notlp_supplier = models.CharField(max_length=100)
    class Meta:
        db_table = "tb_supplier"

    def __str__(self):
        return self.nama_supplier

class customer(models.Model):
    id_customer = models.AutoField(primary_key=True)
    nama_customer = models.CharField(max_length=100)
    alamat_customer = models.CharField(max_length=100)
    notlp_customer= models.CharField(max_length=100)
    class Meta:
        db_table = "tb_customer"

    def __str__(self):
        return self.nama_customer

class merk_brg(models.Model):
    """docstring for merk"""
    id_merk = models.AutoField(primary_key=True)
    nama_merk = models.CharField(max_length=100)
    class Meta:
        db_table = "tb_merk_brg"

    def __str__(self):
        return self.nama_merk

class type_brg(models.Model):
    """docstring for jenis"""
    id_type = models.AutoField(primary_key=True)
    nama_type = models.CharField(max_length=100)

    class Meta:
        db_table = "tb_type_brg"

    def __str__(self):
        return self.nama_type

class barang_masuk(models.Model):
    """docstring for barang_masuk"""
    id_brg_masuk = models.AutoField(primary_key=True)
    kd_barang = models.CharField(max_length=10)
    nm_barang = models.CharField(max_length=100)
    tgl_masuk = models.DateField()
    jml_masuk = models.IntegerField()
    supplier = models.CharField(max_length=100)
    no_resi = models.TextField()
    foto_masuk = models.FileField(upload_to='foto/')

    jenis = models.ForeignKey(jenis_brg, on_delete=models.DO_NOTHING)
    merk = models.ForeignKey(merk_brg, on_delete=models.DO_NOTHING)
    tipe = models.ForeignKey(type_brg, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = "tb_barang_masuk"
    
    def __str__(self):
        return self.nm_barang

# barang keluar
class barang_keluar(models.Model):
    """docstring for barang_keluar"""
    id_brg_keluar = models.AutoField(primary_key=True)
    tgl_keluar = models.DateField()
    sn_barang = models.CharField(max_length=20)
    jml_keluar = models.IntegerField()
    alamat_customer = models.TextField()
    no_bukti = models.CharField(max_length=20)
    no_resi = models.CharField(max_length=20)
    harga_satuan = models.IntegerField()
    total_bayar = models.IntegerField()
    foto_keluar = models.FileField(upload_to='foto/',blank=True)
    kd_brg_keluar = models.CharField(max_length=10)

    nama_barang = models.ForeignKey(barang_masuk,on_delete=models.CASCADE,db_column='nama_barang')
    customer_id = models.ForeignKey(customer,on_delete=models.CASCADE,db_column='customer_id')
    jenis_id = models.ForeignKey(jenis_brg,on_delete=models.CASCADE,db_column='jenis_id')
    merk_id = models.ForeignKey(merk_brg,on_delete=models.CASCADE,db_column='merk_id')
    tipe_id = models.ForeignKey(type_brg,on_delete=models.CASCADE,db_column='tipe_id')

    class Meta:
        db_table = "tb_barang_keluar"

    def __str__(self):
        return self.nm_brg_keluar


class user(models.Model):
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
