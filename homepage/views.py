from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages
from adminhome.models import user

# proses login

def login_view(request):
    if request.POST:
        pengguna = authenticate(username=request.POST['username'], password=request.POST['password'])
        if pengguna is not None:
            if pengguna.is_active:
            	return redirect('/inventaris/')
            else:   
                messages.add_message(request, messages.INFO, 'User belum terverifikasi')
        else:
            messages.add_message(request, messages.INFO, 'Username atau password Anda salah')

    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('/login/')