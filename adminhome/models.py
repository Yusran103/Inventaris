from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.hashers import make_password
from django.db import models

# Create your models here.

class Jenis_brg(models.Model):
    """docstring for jenis"""
    id_jenis = models.AutoField(primary_key=True)
    nama_jenis = models.CharField(max_length=100,unique=True)
    is_deleted = models.CharField(max_length=100,blank=True , null=True)

    class Meta:
        db_table = "tb_jenis_brg"

    def __str__(self):
        return self.nama_jenis

class Supplier(models.Model):
    id_supplier = models.AutoField(primary_key=True)
    nama_supplier = models.CharField(max_length=100,unique=True)
    alamat_supplier = models.CharField(max_length=100)
    notlp_supplier = models.CharField(max_length=100,unique=True)
    is_deleted = models.CharField(max_length=100,blank=True , null=True)
    class Meta:
        db_table = "tb_supplier"
    
    def __str__(self):
        return self.nama_supplier

class Customer(models.Model):
    id_customer = models.AutoField(primary_key=True)
    nama_customer = models.CharField(max_length=100,unique=True)
    alamat_customer = models.CharField(max_length=100)
    notlp_customer= models.CharField(max_length=100)
    is_deleted = models.CharField(max_length=100,blank=True , null=True)
    class Meta:
        db_table = "tb_customer"
    
    def __str__(self):
        return self.nama_customer

class Merk_brg(models.Model):
    """docstring for merk"""
    id_merk = models.AutoField(primary_key=True)
    nama_merk = models.CharField(max_length=100,unique=True)
    is_deleted = models.CharField(max_length=100,blank=True , null=True)
    class Meta:
        db_table = "tb_merk_brg"
    
    def __str__(self):
        return self.nama_merk

class Tipe_brg(models.Model):
    """docstring for jenis"""
    id_tipe = models.AutoField(primary_key=True)
    nama_tipe = models.CharField(max_length=100,unique=True)
    is_deleted = models.CharField(max_length=100,blank=True , null=True)
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
    foto_masuk = models.ImageField(upload_to='foto/',blank=True , null=True) 
    is_deleted = models.CharField(max_length=100,blank=True , null=True)

    supplier_id = models.ForeignKey(Supplier,on_delete=models.CASCADE,db_column='supplier_id')
    jenis_id = models.ForeignKey(Jenis_brg,on_delete=models.CASCADE,db_column='jenis_id')
    merk_id = models.ForeignKey(Merk_brg,on_delete=models.CASCADE,db_column='merk_id')
    tipe_id = models.ForeignKey(Tipe_brg,on_delete=models.CASCADE,db_column='tipe_id')
    

    class Meta:
        db_table = "tb_barang_masuk"
    
    def __str__(self):
        return self.nm_barang


class Barang_keluar(models.Model):
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
    foto_keluar = models.ImageField(upload_to='foto/')
    kd_brg_keluar = models.CharField(max_length=10)
    nm_brg_keluar = models.CharField(max_length=100)
    is_deleted = models.CharField(max_length=100,blank=True , null=True)

    customer_id = models.ForeignKey(Customer,on_delete=models.DO_NOTHING,db_column='customer_id')
    jenis_id = models.ForeignKey(Jenis_brg, on_delete=models.DO_NOTHING,db_column='jenis_id')
    merk_id = models.ForeignKey(Merk_brg, on_delete=models.DO_NOTHING,db_column='merk_id')
    tipe_id = models.ForeignKey(Tipe_brg, on_delete=models.DO_NOTHING,db_column='tipe_id')

    class Meta:
        db_table = "tb_barang_keluar"

    def __str__(self):
        return self.nm_barang

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

    jenis_id = models.ForeignKey(Jenis_brg, on_delete=models.DO_NOTHING,db_column='jenis_id')
    merk_id = models.ForeignKey(Merk_brg, on_delete=models.DO_NOTHING,db_column='merk_id')
    tipe_id = models.ForeignKey(Tipe_brg, on_delete=models.DO_NOTHING,db_column='tipe_id')

    class Meta:
        db_table = "tb_stok"
    
    def __str__(self):
        return self.kd_barang

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError('Email tidak valid')
        if not kwargs.get('username'):
            raise ValueError('Username tidak valid')
        person = self.model(
            email=self.normalize_email(email), username=kwargs.get('username')
        )
        person.set_password(password)
        person.save()
        return person

    def create_superuser(self, email, password, **kwargs):
        person = self.create_user(email, password, **kwargs)

        person.is_superuser = True
        person.is_staff = True
        person.save()

        return person

class User(AbstractBaseUser):
    """docstring for user"""
    USER_CHOICES = [
        ('Admin', 'Admin'),
        ('SuperAdmin', 'SuperAdmin'),
    ]

    id_user = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    nm_lengkap = models.CharField(max_length=255)
    username = models.CharField(max_length=255,unique=True)
    password = models.CharField(max_length=255)
    level = models.CharField(max_length=20, choices=USER_CHOICES, default='SuperAdmin')
    is_deleted = models.CharField(max_length=10,blank=True , null=True,default=False)

    # You may need to add more fields

    is_superuser = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','nm_lengkap']

    def __str__(self):
        return self.username

    def get_full_name(self):
        return '{}'.format(self.nm_lengkap)
    
    def has_perm(self, perm, obj=None):
        return self.is_superuser
    
    def has_module_perms(self, adminhome):
        return self.is_superuser
    
    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super(User, self).save(*args, **kwargs)
    
    class Meta:
        db_table = "tb_user"

