from django.forms import Textarea, ModelForm, NumberInput
from django import forms
from adminhome.models import merk_brg, supplier, type_brg, jenis_brg, customer, barang_keluar

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
        model = merk_brg
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
        model = jenis_brg
        fields = ['nama_jenis']


# -------------+
# TIPE FORM    |
# -------------+

class Typeform(ModelForm):
    nama_type = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Isikan Nama Tipe'
                }
            ),
            required=True
        )
    class Meta:
        model = type_brg
        fields = ['nama_type']

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
        model = supplier
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
        model = customer
        fields = ['nama_customer','alamat_customer','notlp_customer']

# --------------------+
# FORM BARANG KELUAR  |
# -------------------+
class BarangkeluarForm(forms.Form):
    no_bukti = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'No. Bukti Barang'
            }
        ),
        required=True
    )

    nm_brg_keluar = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Nama Barang'
            }
        ),
        required=True
    )

    kd_brg_keluar = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Kode Barang'
            }
        ),
        required=True
    )

    tgl_keluar = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control pull-right',
                'placeholder':'Tanggal Keluar',
                'data-date-format':"dd/mm/yyyy"
            }
        ),
        required=True
    )

    sn_barang = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Serial Number Barang'
            }
        ),
        required=True
    )

    jml_keluar = forms.IntegerField(
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

    total_bayar = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Total Bayar'
            }
        ),
        required=True
    )

    Customer = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Customer'
            }
        ),
        required=True
    )

    alamat_customer = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Alamat Customer'
            }
        ),
        required=True
    )

    no_resi = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'No. Resi'
            }
        ),
        required=True
    )

    merk_id = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Merk'
            }
        ),
        required=True
    )

    jenis_id = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Jenis'
            }
        ),
        required=True
    )

    tipe_id = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Tipe'
            }
        ),
        required=True
    )

    foto_keluar = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Foto'
            }
        ),
        required=True
    )

    class Meta:
        model = barang_keluar
        fields = ['no_bukti','nm_brg_keluar','kd_brg_keluar','tgl_keluar','sn_barang','jml_keluar','harga_satuan','total_bayar','Customer','alamat_customer','no_resi','merk_id','jenis_id','tipe_id','foto_keluar']
