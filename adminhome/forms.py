from django.forms import Textarea, ModelForm, ModelChoiceField
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

    class Meta:
        model = barang_keluar
        fields = ['no_bukti']
