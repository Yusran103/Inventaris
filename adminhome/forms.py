from django.forms import Textarea, ModelForm, Select
from django import forms
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _
from adminhome.models import merk_brg, supplier, type_brg, jenis_brg, customer, user

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
# TIPE MERK    |
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
        widget=forms.TextInput(
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
        widget=forms.TextInput(
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

# ---------------+
# FORM Add User  |
# ---------------+

class Userform(ModelForm):
    class Meta:
        model = user
        fields = ['nm_lengkap', 'username', 'password', 'level']
        labels = {
            'nm_lengkap':"Nama",
            'username':'Username',
            'password':'Password',
            'level':'Level',
        }
        error_messages = {
            'nm_lengkap': {
                'required': 'Nama belum terisi'
            },
            'username' : {
                'required': "Anda harus mengisi username"
            },
            'password' : {
                'required': "Anda harus mengisi password"
            },
            'level':{
                'required': "Anda harus memilih level akun"
            }
        }
        widgets = {
            'nm_lengkap': forms.TextInput(attrs={'class':'form-control','placeholder':'masukan nama'}),
            'username': forms.TextInput(attrs={'class':'form-control','placeholder':'masukan username'}),
            'password': forms.PasswordInput(attrs={'class':'form-control','placeholder':'masukan password'}),
            'level': forms.Select(attrs={'class':'form-control','placeholder':'pilih Level Akun'}),
        }