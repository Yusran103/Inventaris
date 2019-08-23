from django.forms.models import ModelMultipleChoiceField
from django.forms import Textarea, ModelForm, Select
from django import forms
from adminhome.models import Merk_brg, Supplier, Tipe_brg, Jenis_brg, Customer, Barang_masuk, Stok_barang, Akun, Barangkeluar, Barang_retur
from django.contrib.auth.models import User

# -------------+
# FORM MERK    |
# -------------+
class Merkform(ModelForm):
    nama_merk = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Isikan Nama Merk',
                'autofocus': 'True'
                }
            ),
            required=True
        )
    class Meta:
        model = Merk_brg
        fields = ['nama_merk']

# -------------+
# JENIS FORM   |
# -------------+
class Jenisform(ModelForm):
    nama_jenis = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Isikan Nama Jenis',
                'autofocus': 'True'
                }
            ),
            required=True
        )
    class Meta:
        model = Jenis_brg
        fields = ['nama_jenis']


# -------------+
# TIPE FORM    |
# -------------+

class Tipeform(ModelForm):
    nama_tipe = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Isikan Nama Tipe',
                'autofocus': 'True'
                }
            ),
            required=True
        )
    class Meta:
        model = Tipe_brg
        fields = ['nama_tipe']

# ---------------+
# FORM SUPPLIER  |
# ---------------+
class Supplierform(ModelForm):
    nama_supplier = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Isikan Nama Supplier',
                'autofocus': 'True'
                }
            ),
            required=True
        )
    alamat_supplier = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class':'form-control',
                'placeholder':'Isikan Alamat Customer',
                'rows':'3',
                # 'id':'demo9'
                # 'disabled':''
            }
        ),
        )

    notlp_supplier = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Isikan Nomor Hp Supplier'
                }
            ),
            required=True
        )

    class Meta:
        model = Supplier
        fields = ['nama_supplier','alamat_supplier','notlp_supplier']

# ---------------+
# FORM CUSTOMER  |
# ---------------+
class Customerform(ModelForm):
    nama_customer = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Isikan Nama Customer',
                'autofocus': 'True'
                }
            ),
            required=True
        )
    alamat_customer = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class':'form-control',
                'placeholder':'Alamat Customer',
                'rows':'3',
                # 'id':'demo9'
                # 'disabled':''
            }
        ),
            required=True
        )

    notlp_customer = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Isikan Nomor Hp Customer'
                }
            ),
            required=True
        )

    class Meta:
        model = Customer
        fields = ['nama_customer','alamat_customer','notlp_customer']

# ------------+
# BRG MSK FORM|
# ------------+
class Barang_masuk_form(ModelForm):
    kd_barang = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Isikan Kode Barang',
                'autofocus': 'True'
                }
            ),
        )
    nm_barang = forms.CharField(
        widget= forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Isikan Nama Barang',
                'autofocus': 'True'
                }
            ),
        )
    tgl_masuk = forms.DateField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control tgl_masuk',
                'placeholder':'Isikan Tanggal masuk Barang',
                'id':'datepicker',
                }
            ),
        )
    jml_masuk = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'type' : 'number',
                'min' : '1',
                'placeholder':'Isikan Jumlah Barang'
                }
            ),
        )
    supplier_id = forms.ModelChoiceField(
        queryset = Supplier.objects.filter(is_deleted='False')
        )
    no_resi = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Isikan nomor resi'
                }
            ),
        )
    harga_satuan = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Isikan Harga Barang'
                }
            ),
        )
    foto_masuk = forms.FileField(
        )
    jenis_id = forms.ModelChoiceField(
        queryset = Jenis_brg.objects.filter(is_deleted='False')
        )
    merk_id = forms.ModelChoiceField(
        queryset = Merk_brg.objects.filter(is_deleted='False')
        )
    tipe_id = forms.ModelChoiceField(
        queryset = Tipe_brg.objects.filter(is_deleted='False')
        )
    
    class Meta:
        model = Barang_masuk
        fields = [
            'kd_barang',
            'nm_barang',
            'tgl_masuk',
            'harga_satuan',
            'jml_masuk',
            'supplier_id',
            'no_resi',
            'foto_masuk',
            'jenis_id',
            'merk_id',
            'tipe_id'
            ]

# --------------------+
# FORM BARANG KELUAR  |
# -------------------+
class BarangkeluarForm(ModelForm):
    no_bukti = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'No. Bukti Barang',
                'autofocus': 'True'
            }
        ),
        required=True
    )

    nama_barang = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Kode Barang',
                # 'id':'demo',
                # 'disabled':''
            }
        ),
        required=True
    )

    kode_barang = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Kode Barang',
                # 'id':'demo1',
                # 'disabled':''
            }
        ),
        required=True
    )

    tanggal = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control pull-right',
                'placeholder':'Tanggal Keluar',
                'data-date-format':"yyyy/mm/dd",
                'id':'date',
                'autocomplete':'off',
            }
        ),
        required=True
    )

    serialnumber = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Serial Number Barang',
                # 'id':'demo2',
                # 'disable':''
            }
        ),
        required=True
    )

    no_resi = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'No. Resi',
                # 'id':'demo3',
                # 'disabled':''
            }
        ),
        required=True
    )

    jumlah = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Jumlah Barang',
                'min' : '0',
                'id':'jumlah'
            }
        ),
        required=True
    )

    harga_satuan = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Harga Satuan',
                # 'id':'demo4',
                # 'disabled':''
            }
        ),
        required=True
    )

    total_bayar = forms.IntegerField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Total Bayar',
                'id':'totalbayar',
                # 'disabled':''
            }
        ),
        required=True
    )

    alamat_customer = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class':'form-control',
                'placeholder':'Alamat Customer',
                'rows':'3',
                # 'id':'demo9'
                # 'disabled':''
            }
        ),
        required=True
    )

    customer_id = forms.ModelChoiceField(
        queryset = Customer.objects.filter(is_deleted='False'),
        # to_field_name="nama_jenis",
        widget=Select(
            attrs={
                # 'style':'width: 100%',
                'class':'form-control',
                # 'id':'demo8'
                })
        )

    jenis_id = forms.ModelChoiceField(
        queryset = Jenis_brg.objects.filter(is_deleted='False'),
        # to_field_name="nama_jenis",
        widget=Select(
            attrs={
                # 'style':'width: 100%',
                'class':'form-control',
                # 'id':'demo6'
                })
        )

    merk_id = forms.ModelChoiceField(
        queryset = Merk_brg.objects.filter(is_deleted='False'),
        # to_field_name="nama_merk"
        widget=Select(
            attrs={
                # 'style':'width: 100%',
                'class':'form-control',
                # 'id':'demo5'
                })
        )

    tipe_id = forms.ModelChoiceField(
        queryset = Tipe_brg.objects.filter(is_deleted='False'),
        # to_field_name="nama_tipe"
        widget=Select(
            attrs={
                # 'style':'width: 100%',
                'class':'form-control',
                # 'id':'demo7'
                })
        )

    foto_keluar = forms.FileField(
        required=True
    )

    class Meta:
        model = Barangkeluar
        fields = "__all__"


# ----------+
# STOK FORM |
# ----------+
class Stok_form(ModelForm):
    class Meta:
        model = Stok_barang
        fields = [
            'tanggal',
            'nm_barang',
            'kd_barang',
            'hrg_barang',
            'jumlah_stok',
            'stok_akhir',
            'keterangan',
            'jenis_id',
            'merk_id',
            'tipe_id'
            ]

# ----------+
# User FORM |
# ----------+
class User_form(ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Isikan nama awal',
                'autofocus': 'True'
                }
            ),
            required=True
        )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Isikan nama akhir'
                }
            ),
            required=True
        )
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Isikan username'
                }
            ),
            required=True
        )
    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder':'Isikan email'
                }
            ),
            required=True
        )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'Isikan password'
                }
            ),
            required=True
        )
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password'
        ]

class Akun_form(ModelForm):
    class Meta:
        model = Akun
        fields = [
            'level'
        ]

class Barang_retur_form(ModelForm):
    nm_barang = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Isikan nama barang',
                'autofocus': 'True'
                }
            ),
            required=True
        )
    kd_barang = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Isikan kode barang',
                'autofocus': 'True'
                }
            ),
            required=True
        )
    no_bukti = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Isikan nomor bukti'
                }
            ),
            required=True
        )
    sn_barang = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Isikan Serial Number'
                }
            ),
            required=True
        )
    tanggal = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Tanggal  ',
                'data-date-format':"yyyy/mm/dd",
                'id':'datepicker',
                'autocomplete':'off',
            }
        ),
        required=True
    )
    supplier_id = forms.ModelChoiceField(
        queryset = Supplier.objects.filter(is_deleted='False'),
        # to_field_name="nama_jenis",
        widget=Select(
            attrs={
                # 'style':'width: 100%',
                'class':'form-control',
                # 'id':'demo6'
                })
        )

    customer_id = forms.ModelChoiceField(
        queryset = Customer.objects.filter(is_deleted='False'),
        # to_field_name="nama_jenis",
        widget=Select(
            attrs={
                # 'style':'width: 100%',
                'class':'form-control',
                # 'id':'demo6'
                })
        )

    jenis_id = forms.ModelChoiceField(
        queryset = Jenis_brg.objects.filter(is_deleted='False'),
        # to_field_name="nama_jenis",
        widget=Select(
            attrs={
                # 'style':'width: 100%',
                'class':'form-control',
                # 'id':'demo6'
                })
        )

    merk_id = forms.ModelChoiceField(
        queryset = Merk_brg.objects.filter(is_deleted='False'),
        # to_field_name="nama_merk"
        widget=Select(
            attrs={
                # 'style':'width: 100%',
                'class':'form-control',
                # 'id':'demo5'
                })
        )

    tipe_id = forms.ModelChoiceField(
        queryset = Tipe_brg.objects.filter(is_deleted='False'),
        # to_field_name="nama_tipe"
        widget=Select(
            attrs={
                # 'style':'width: 100%',
                'class':'form-control',
                # 'id':'demo7'
                })
        )
    
    foto = forms.FileField(
        required=True
    )

    class Meta:
        model = Barang_retur
        fields = [
            'nm_barang',
            'kd_barang',
            'no_bukti',
            'sn_barang',
            'tanggal',
            'supplier_id',
            'merk_id',
            'jenis_id',
            'tipe_id',
            'customer_id',
            'foto'
            ]