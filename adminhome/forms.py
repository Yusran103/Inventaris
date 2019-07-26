from django.forms import Textarea, ModelForm
from django import forms
from adminhome.models import Merk_brg, Supplier, Tipe_brg, Jenis_brg, Customer, Barang_masuk, Barangkeluar


# -------------+
# FORM MERK    |
# -------------+
class Merkform(ModelForm):
    nama_merk = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Isikan Nama Merk'
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
                'placeholder':'Isikan Nama Jenis'
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
                'placeholder':'Isikan Nama Tipe'
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
                'placeholder':'Isikan Nama Supplier'
                }
            ),
            required=True
        )
    alamat_supplier = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class':'form-control',
                'placeholder':'Isikan Alamat Supplier'
                }
            ),
            required=True
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
                'placeholder':'Isikan Nama Customer'
                }
            ),
            required=True
        )
    alamat_customer = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class':'form-control',
                'placeholder':'Isikan Alamat Customer'
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

# --------------------+
# FORM BARANG KELUAR  |
# -------------------+
class BarangkeluarForm(ModelForm):
    no_bukti = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'No. Bukti Barang'
            }
        ),
        required=True
    )

    # nama_barang = forms.ModelChoiceField(
    #     queryset = Barang_masuk.objects.all(),
    # )

    # kode_barang = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             'class':'form-control',
    #             'placeholder':'Kode Barang',
    #             # 'disabled':''
    #         }
    #     ),
    #     required=True
    # )

    tanggal = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control pull-right',
                'placeholder':'Tanggal Keluar',
                'data-date-format':"yyyy/mm/dd",
                'id':'date'
            }
        ),
        required=True
    )

    # serialnumber = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             'class':'form-control',
    #             'placeholder':'Serial Number Barang',
    #             'disable/d':''
    #         }
    #     ),
    #     required=True
    # )

    jumlah = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Jumlah Barang'
            }
        ),
        required=True
    )

    harga_satuan = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Harga Satuan'
            }
        ),
        required=True
    )

    total_bayar = forms.IntegerField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Total Bayar',
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
                # 'disabled':''
            }
        ),
        required=True
    )

    no_resi = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'No. Resi',
                # 'disabled':''
            }
        ),
        required=True
    )

    customer_id = forms.ModelChoiceField(
        queryset = Customer.objects.all(),
        required=True
    )

    # merk_id = forms.ModelChoiceField(
    #     queryset = Merk_brg.objects.all(),required=True
    # )

    # jenis_id = forms.ModelChoiceField(
    #     queryset = Jenis_brg.objects.all(),required=True
    # )

    # tipe_id = forms.ModelChoiceField(
    #     queryset = Tipe_brg.objects.all(),required=True
    # )

    foto_keluar = forms.FileField(
        required=True
    )

    class Meta:
        model = Barangkeluar
        fields = "__all__"

# ------------+
# BRG MSK FORM|
# ------------+

class Barang_masuk_form(ModelForm):
    kd_barang = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Isikan Kode Barang'
                }
            ),
        )
    nm_barang = forms.CharField(
        widget= forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Isikan Nama Barang'
                }
            ),
        )
    sn_barang = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Isikan Serial Number Barang'
                }
            ),
        )
    tgl_masuk = forms.DateField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control tgl_masuk',
                'placeholder':'Isikan Tanggal masuk Barang',
                'id':'datepicker'
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
        queryset = Supplier.objects.all()
        )
    no_resi = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Isikan nomor resi'
                }
            ),
        )
    # foto_masuk = forms.FileField(
    #     )
    jenis_id = forms.ModelChoiceField(
        queryset = Jenis_brg.objects.all()
        )
    merk_id = forms.ModelChoiceField(
        queryset = Merk_brg.objects.all()
        )
    tipe_id = forms.ModelChoiceField(
        queryset = Tipe_brg.objects.all()
        )
    
    class Meta:
        model = Barang_masuk
        fields = [
            'kd_barang',
            'nm_barang',
            'sn_barang',
            'tgl_masuk',
            'jml_masuk',
            'supplier_id',
            'no_resi',
            'foto_masuk',
            'jenis_id',
            'merk_id',
            'tipe_id'
            ]

