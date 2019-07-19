from django.forms import ModelForm, Textarea
from django import forms
from adminhome.models import merk_brg, jenis_brg

# -------------+
# FORM MERK    |
# -------------+


class Merkform(ModelForm):
    class Meta:
        model = merk_brg
        fields = ['nama_merk']
        label = {
            'nama_merk': "Nama Merk",
        }

        error_messages = {
            'nama_merk': {
                'required': 'Tolong Isikan Nama Merk'
            },
        }
        widget = {
            'nama_merk': forms.Textarea(attrs={'cols': 50, 'rows': 5, 'class': 'form-control pull-left'}),
        }
