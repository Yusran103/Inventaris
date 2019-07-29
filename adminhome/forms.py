from django.forms import Textarea, ModelForm 
from django import forms
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _
from adminhome.models import merk_brg, supplier, type_brg, jenis_brg, customer, user


# -------------+
# FORM LOGIN    |
# -------------+
class Loginform(ModelForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
            'class':'form-control',
            'placeholder':'Username'
            }
            ),
        required=True
        )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
            'class':'form-control',
            'placeholder':'Password'
            }
            ),
        required=True
        )    
    class Meta:
        model = user
        fields = ['username', 'password']

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
        fields = ['nm_lengkap', 'username', 'level', 'password']
        labels = {
            'nm_lengkap':"Nama",
            'username':'Username',
            'level':'Level',
            'password':'Password',
        }
        error_messages = {
            'nm_lengkap': {
                'required': 'masukan nama'
            },
            'username' : {
                'required': "Anda harus masukan username"
            },
            'level' : {
                'required': "Anda harus memilih level"
            },
            'password':{
                'required': "Masukan password"
            }
        }
        widgets = {
            'level':forms.Select (attrs={ 'class':'form-control' }),
            'username':forms.TextInput (attrs={ 'class':'form-control' }),
            'nm_lengkap':forms.TextInput (attrs={ 'class':'form-control' }),
            'password': forms.PasswordInput(attrs={ 'class':'form-control' })

        }

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = settings.SIGN_UP_FIELDS

    email = forms.EmailField(label=_('Email'), help_text=_('Required. Enter an existing email address.'))

    def clean_email(self):
        email = self.cleaned_data['email']

        user = User.objects.filter(email__iexact=email).exists()
        if user:
            raise ValidationError(_('You can not use this email address.'))

        return email