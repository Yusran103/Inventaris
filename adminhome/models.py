from django.db import models

# Create your models here.

class jenis_brg(models.Model):
    """docstring for jenis"""
    id_jenis = models.AutoField(primary_key=True)
    nama_jenis = models.CharField(max_length=100)

    class Meta:
        db_table = "tb_jenis_brg"

class supplier(models.Model):
    id_supplier = models.AutoField(primary_key=True)
    nama_supplier = models.CharField(max_length=100)
    alamat_supplier = models.CharField(max_length=100)
    notlp_supplier = models.CharField(max_length=100)
    class Meta:
        db_table = "tb_supplier"

class customer(models.Model):
    id_customer = models.AutoField(primary_key=True)
    nama_customer = models.CharField(max_length=100)
    alamat_customer = models.CharField(max_length=100)
    notlp_customer= models.CharField(max_length=100)
    class Meta:
        db_table = "tb_customer"

class merk_brg(models.Model):
    """docstring for merk"""
    id_merk = models.AutoField(primary_key=True)
    nama_merk = models.CharField(max_length=100)
    class Meta:
        db_table = "tb_merk_brg"

class type_brg(models.Model):
    """docstring for jenis"""
    id_type = models.AutoField(primary_key=True)
    nama_type = models.CharField(max_length=100)

    class Meta:
        db_table = "tb_type_brg"

class barang_masuk(models.Model):
    """docstring for barang_masuk"""
    id_brg_masuk = models.AutoField(primary_key=True)
    kd_barang = models.CharField(max_length=10)
    nm_barang = models.CharField(max_length=100)
    tgl_masuk = models.DateField()
    jml_masuk = models.IntegerField()
    supplier = models.CharField(max_length=100)
    no_resi = models.TextField()
    foto_masuk = models.TextField() 

    jenis = models.ForeignKey(jenis_brg, on_delete=models.DO_NOTHING)
    merk = models.ForeignKey(merk_brg, on_delete=models.DO_NOTHING)
    tipe = models.ForeignKey(type_brg, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = "tb_barang_masuk"


class barang_keluar(models.Model):
    """docstring for barang_keluar"""
    id_brg_keluar = models.AutoField(primary_key=True)
    tgl_keluar = models.DateField()
    sn_barang = models.CharField(max_length=20)
    jml_keluar = models.IntegerField()
    Customer = models.CharField(max_length=25)
    alamat_customer = models.TextField()
    no_bukti = models.CharField(max_length=20)
    no_resi = models.CharField(max_length=20)
    harga_satuan = models.IntegerField()
    total_bayar = models.IntegerField()
    foto_keluar = models.TextField()
    kd_brg_keluar = models.CharField(max_length=10)
    nm_brg_keluar = models.CharField(max_length=100)

    jenis = models.ForeignKey(jenis_brg, on_delete=models.DO_NOTHING)
    merk = models.ForeignKey(merk_brg, on_delete=models.DO_NOTHING)
    tipe = models.ForeignKey(type_brg, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = "tb_barang_keluar"


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
