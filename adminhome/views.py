from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from adminhome.models import merk_brg , jenis_brg , supplier , type_brg , customer
from adminhome.forms import Merkform , Supplierform , Typeform, Jenisform, Customerform, Userform
from django.core.paginator import Paginator
from django.contrib import auth
from adminhome.models import user
from django.conf import settings
from django.utils.crypto import get_random_string
from django.views.generic import View, FormView
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.decorators import login_required
import bcrypt
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

#---------+
# LOGIN   |
# --------+

def index(request):
    return render(request, 'login.html')

def login_view(request):
    if (user.objects.filter(username=request.POST['login_username']).exists()):
        akun = user.objects.filter(username=request.POST['login_username'])[0]
        if (bcrypt.checkpw(request.POST['login_password'].encode(), akun.password.encode())):
            request.session['nm_lengkap'] = akun.nm_lengkap
            request.session['username'] = akun.username  
            request.session['level'] = akun.level
            request.session['password'] = akun.password
            request.session['id_user'] = akun.id_user            
            return redirect('/inventaris/')
        else:
            messages.add_message(request, messages.INFO, 'Username atau password Anda salah')
    return render(request, 'login.html')

#-----------+
#    USER   |
# ----------+

def logout_view(request):
    logout(request)
    return render(request, 'login.html')

def cariuser(request):
    pengguna = request.GET.get('cari')
    daftar_user = user.objects.filter(
            Q(nm_lengkap__icontains=pengguna) | Q(username__icontains=pengguna) |
            Q(level__icontains=pengguna)
        ).order_by('nm_lengkap')
    pagination = Paginator(daftar_user,10)
    page = request.GET.get('page')
    try:
        posts = pagination.page(page)
    except PageNotAnInteger:
        posts = pagination.page(1)
    except EmptyPage:
        posts = pagination.page(pagination.num_pages)
    
    context = {
        'daftar_users': posts,
        'users':pengguna
    }
    return render(request, 'users/view-user.html', context)

def viewuser(request):
    daftar_user = user.objects.all()
    pagination = Paginator(daftar_user,10)
    page = request.GET.get('page','')
    user_pg = pagination.get_page(page)
    return render(request, 'users/view-user.html',{'daftar_users': user_pg})

def register(request):
    if request.method == 'POST':
        form_data = request.POST
        form = Userform(form_data)
        if form.is_valid():
            hashed_password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
            akun = user(nm_lengkap=request.POST['nm_lengkap'], username=request.POST['username'], password=hashed_password.decode('utf-8'), level=request.POST['level'])
            akun.save()
            return redirect('/inventaris/users')
    else:
        form = Userform()
    return render(request, 'users/add-user.html', {'form': form})

def edituser(request,pk):
    User = user.objects.get(pk=pk)
    if request.method == "POST":
        form = Userform(request.POST, instance=User)
        if form.is_valid():
            User = form.save(commit=False)
            nm_lengkap = request.POST['nm_lengkap']
            username = request.POST['username']
            level = request.POST['level']
            password = request.POST['password']
            User.save()
            return redirect('/inventaris/users', pk=User.pk)
    else:
        form = Userform(instance=User)
    return render(request, 'users/edit-user.html', {'form': form, 'user' : User})

def deleteuser(request,pk):
    User = user.objects.get(pk=pk)
    User.delete()
    return redirect('/inventaris/users')

def changepassword(request,pk):
    User = user.objects.get(pk = request.session['id_user'])
    if request.method == "POST":
        form = Userform(request.POST, instance=User)
        if form.is_valid():
            hashed_password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
            akun = User(password=hashed_password.decode('utf-8'))
            akun.save()
            return redirect('/inventaris/')
    else:
        form = Userform(instance=User)
    return render(request, 'changepassword.html', {'form': form, 'user' : User})

# -----------+
# DASHBOARD  |
# -----------+

def dashboard(request):
    Ssn = request.session
    if Ssn is not None :
        for key, value in request.session.items():
            print('{} => {}'.format(key, value))
        return render(request, 'dashboard.html')
    else :
        return render(request, 'login.html')
        

# -----------+
# STOK       |
# -----------+


def gridstok(request):
    return render(request, 'transaksi/stok/viewgrid-stok.html')


def stok(request):
    return render(request, 'transaksi/stok/view-stok.html')

# ------------+
# BARANG MASUK|
# ------------+


def barangmasuk(request):
    return render(request, 'transaksi/masuk/view-barang-masuk.html')


def barangmasukgrid(request):
    return render(request, 'transaksi/masuk/viewgrid-barang-masuk.html')


def editbarangmasuk(request):
    return render(request, 'transaksi/masuk/edit-barang-masuk.html')


def tambahbarangmasuk(request):
    return render(request, 'transaksi/masuk/add-barang-masuk.html')

# -------------+
# BARANG KELUAR|
# -------------+


def barangkeluar(request):
    
    return render(request, 'transaksi/keluar/view-barang-keluar.html')


def barangkeluargrid(request):
    return render(request, 'transaksi/keluar/viewgrid-barang-keluar.html')


def editbarangkeluar(request):
    return render(request, 'transaksi/keluar/edit-barang-keluar.html')


def tambahbarangkeluar(request):
    return render(request, 'transaksi/keluar/add-barang-keluar.html')

# -------------+
# LAPORAN      |
# -------------+


def laporanmasuk(request):
    return render(request, 'laporan/laporan-barang-masuk.html')


def laporankeluar(request):
    return render(request, 'laporan/laporan-barang-keluar.html')


def laporanstok(request):
    return render(request, 'laporan/laporan-barang-stok.html')

# ---------------+
# CHANGE PASSWORD|
# ---------------+

# -------------+
# MASTER DATA  |
# -------------+

def carimerk(request):
    merk = request.GET.get('cari')
    daftar_merk = merk_brg.objects.filter(
            Q(nama_merk__icontains=merk)
        ).order_by('nama_merk')
    pagination = Paginator(daftar_merk,10)
    page = request.GET.get('page')
    try:
        posts = pagination.page(page)
    except PageNotAnInteger:
        posts = pagination.page(1)
    except EmptyPage:
        posts = pagination.page(pagination.num_pages)
    
    context = {
        'daftar_merk': posts,
        'key_merk':merk
    }
    return render(request, 'masterdata/merk/merk.html', context)

def viewmerk(request):
    daftar_merk = merk_brg.objects.all()
    pagination = Paginator(daftar_merk,10)

    page = request.GET.get('page','')
    merk_pg = pagination.get_page(page)
    return render(request, 'masterdata/merk/merk.html', {'daftar_merk': merk_pg})


def addmerk(request):
    if request.method == 'POST':
        form_data = request.POST
        form = Merkform(form_data)
        if form.is_valid():
            Merk = merk_brg(
                nama_merk=request.POST['nama_merk']
            )
            Merk.save()
            return redirect('/inventaris/masterdata/merk')
    else:
        form = Merkform()
    return render(request, 'masterdata/merk/merk_tambah.html', {'form': form})


def editmerk(request,pk):
    Merk = merk_brg.objects.get(pk=pk)
    if request.method == "POST":
        form = Merkform(request.POST, instance=Merk)
        if form.is_valid():
            Merk = form.save(commit=False)
            nama_merk = request.POST['nama_merk']
            Merk.save()
            return redirect('/inventaris/masterdata/merk', pk=Merk.pk)
    else:
        form = Merkform(instance=Merk)
    return render(request, 'masterdata/merk/merk_edit.html', {'form': form, 'merk' : Merk})

def deletemerk(request,pk):
    Merk = merk_brg.objects.get(pk=pk)
    Merk.delete()
    return redirect('/inventaris/masterdata/merk')

# ------------+
#     jENIS   |
# ------------+

def carijenis(request):
    jenis = request.GET.get('cari')
    daftar_jenis = jenis_brg.objects.filter(
            Q(nama_jenis__icontains=jenis)
        ).order_by('nama_jenis')
    pagination = Paginator(daftar_jenis,10)
    page = request.GET.get('page')
    try:
        posts = pagination.page(page)
    except PageNotAnInteger:
        posts = pagination.page(1)
    except EmptyPage:
        posts = pagination.page(pagination.num_pages)
    
    context = {
        'daftar_jenis': posts,
        'key_jenis':jenis
    }
    return render(request, 'masterdata/jenis/jenis.html', context)

def viewjenis(request):
    daftar_jenis = jenis_brg.objects.all()
    pagination = Paginator(daftar_jenis,10)

    page = request.GET.get('page','')
    jenis_pg = pagination.get_page(page)
    return render(request, 'masterdata/jenis/jenis.html', {'daftar_jenis': jenis_pg})

def addjenis(request):
    if request.method == 'POST':
        form_data = request.POST
        form = Jenisform(form_data)
        if form.is_valid():
            Jenis = jenis_brg(
                nama_jenis=request.POST['nama_jenis']
            )
            Jenis.save()
            return redirect('/inventaris/masterdata/jenis')
    else:
        form = Jenisform()
    return render(request, 'masterdata/jenis/jenis_tambah.html', {'form': form})

def editjenis(request,pk):
    Jenis = jenis_brg.objects.get(pk=pk)
    if request.method == "POST":
        form = Jenisform(request.POST, instance=Jenis)
        if form.is_valid():
            Jenis = form.save(commit=False)
            nama_jenis = request.POST['nama_jenis']
            Jenis.save()
            return redirect('/inventaris/masterdata/jenis', pk=Jenis.pk)
    else:
        form = Jenisform(instance=Jenis)
    return render(request, 'masterdata/jenis/jenis_edit.html', {'form': form, 'jenis' : Jenis})

def deletejenis(request,pk):
    jenis = jenis_brg.objects.get(pk=pk)
    jenis.delete()
    return redirect('/inventaris/masterdata/jenis')

# ------------+
#    SUPLIER  |
# ------------+

def carisuplier(request):
    suplier = request.GET.get('cari')
    daftar_supplier = supplier.objects.filter(
            Q(nama_supplier__icontains=suplier) | Q(alamat_supplier__icontains=suplier) |
            Q(notlp_supplier__icontains=suplier)
        ).order_by('nama_supplier')
    pagination = Paginator(daftar_supplier,10)
    page = request.GET.get('page')
    try:
        posts = pagination.page(page)
    except PageNotAnInteger:
        posts = pagination.page(1)
    except EmptyPage:
        posts = pagination.page(pagination.num_pages)
    
    context = {
        'daftar_supplier': posts,
        'key_suplier':suplier
    }
    return render(request, 'masterdata/supplier/supplier.html', context)

def viewsupplier(request):
    daftar_supplier = supplier.objects.all()
    pagination = Paginator(daftar_supplier,10)

    page = request.GET.get('page','')
    supplier_pg = pagination.get_page(page)
    return render(request, 'masterdata/supplier/supplier.html', {'daftar_supplier': supplier_pg})

def addsupplier(request):
    if request.method == 'POST':
        form_data = request.POST
        form = Supplierform(form_data)
        if form.is_valid():
            Supplier = supplier(
                nama_supplier=request.POST['nama_supplier'],
                alamat_supplier=request.POST['alamat_supplier'],
                notlp_supplier=request.POST['notlp_supplier']
            )
            Supplier.save()
            return redirect('/inventaris/masterdata/supplier')
    else:
        form = Supplierform()
    return render(request, 'masterdata/supplier/supplier_tambah.html', {'form': form})

def editsupplier(request,pk):
    Supplier = supplier.objects.get(pk=pk)
    if request.method == "POST":
        form = Supplierform(request.POST, instance=Supplier)
        if form.is_valid():
            Supplier = form.save(commit=False)
            nama_supplier = request.POST['nama_supplier']
            alamat_supplier = request.POST['alamat_supplier']
            notlp_supplier = request.POST['notlp_supplier']
            Supplier.save()
            return redirect('/inventaris/masterdata/supplier', pk=Supplier.pk)
    else:
        form = Supplierform(instance=Supplier)
    return render(request, 'masterdata/supplier/supplier_edit.html', {'form': form, 'supplier' : Supplier})

def deletesupplier(request,pk):
    Supplier = supplier.objects.get(pk=pk)
    Supplier.delete()
    return redirect('/inventaris/masterdata/supplier')

# ------------+
#   CUSTOMER  |
# ------------+

def caricustomer(request):
    customers = request.GET.get('cari')
    daftar_customer = customer.objects.filter(
            Q(nama_customer__icontains=customers) | Q(alamat_customer__icontains=customers) |
            Q(notlp_customer__icontains=customers)
        ).order_by('nama_customer')
    pagination = Paginator(daftar_customer,10)
    page = request.GET.get('page')
    try:
        posts = pagination.page(page)
    except PageNotAnInteger:
        posts = pagination.page(1)
    except EmptyPage:
        posts = pagination.page(pagination.num_pages)
    
    context = {
        'daftar_customer': posts,
        'key_customer':customers
    }
    return render(request, 'masterdata/customer/customer.html', context)

def viewcustomer(request):
    daftar_customer = customer.objects.all()
    pagination = Paginator(daftar_customer,10)
    page = request.GET.get('page','')
    customer_pg = pagination.get_page(page)
    return render(request, 'masterdata/customer/customer.html',{'daftar_customer': customer_pg})

def addcustomer(request):
    if request.method == 'POST':
        form_data = request.POST
        form = Customerform(form_data)
        if form.is_valid():
            Customer = customer(
                nama_customer= request.POST['nama_customer'],
                alamat_customer=request.POST['alamat_customer'],
                notlp_customer=request.POST['notlp_customer']
            )
            Customer.save()
            return redirect('/inventaris/masterdata/customer')
    else:
        form = Customerform()
    return render(request, 'masterdata/customer/customer_tambah.html', {'form': form})

def editcustomer(request,pk):
    Customer = customer.objects.get(pk=pk)
    if request.method == "POST":
        form = Customerform(request.POST, instance=Customer)
        if form.is_valid():
            Customer = form.save(commit=False)
            nama_customer = request.POST['nama_customer']
            alamat_customer = request.POST['alamat_customer']
            notlp_customer = request.POST['notlp_customer']
            Customer.save()
            return redirect('/inventaris/masterdata/customer', pk=Customer.pk)
    else:
        form = Customerform(instance=Customer)
    return render(request, 'masterdata/customer/customer_edit.html', {'form': form, 'customer' : Customer})

def deletecustomer(request,pk):
    Customer = customer.objects.get(pk=pk)
    Customer.delete()
    return redirect('/inventaris/masterdata/customer')

# ----------+
#    TIPE   |
# ----------+

def caritipe(request):
    tipe = request.GET.get('cari')
    daftar_tipe = type_brg.objects.filter(
            Q(nama_type__icontains=tipe)
        ).order_by('nama_type')
    pagination = Paginator(daftar_tipe,10)
    page = request.GET.get('page')
    try:
        posts = pagination.page(page)
    except PageNotAnInteger:
        posts = pagination.page(1)
    except EmptyPage:
        posts = pagination.page(pagination.num_pages)
    
    context = {
        'daftar_tipe': posts,
        'key_tipe':tipe
    }
    return render(request, 'masterdata/tipe/tipe.html', context)

def viewtipe(request):
    daftar_tipe = type_brg.objects.all()
    pagination = Paginator(daftar_tipe,10)

    page = request.GET.get('page','')
    tipe_pg = pagination.get_page(page)
    return render(request, 'masterdata/tipe/tipe.html',{'daftar_tipe': tipe_pg})

def addtipe(request):
    if request.method == 'POST':
        form_data = request.POST
        form = Typeform(form_data)
        if form.is_valid():
            Tipe = type_brg(
                nama_type=request.POST['nama_type']
            )
            Tipe.save()
            return redirect('/inventaris/masterdata/tipe')
    else:
        form = Typeform()
    return render(request, 'masterdata/tipe/tipe_tambah.html', {'form': form})

def edittipe(request,pk):
    Tipe = type_brg.objects.get(pk=pk)
    if request.method == "POST":
        form = Typeform(request.POST, instance=Tipe)
        if form.is_valid():
            Tipe = form.save(commit=False)
            nama_type= request.POST['nama_type']
            Tipe.save()
            return redirect('/inventaris/masterdata/tipe', pk=Tipe.pk)
    else:
        form = Typeform(instance=Tipe)
    return render(request, 'masterdata/tipe/tipe_edit.html', {'form': form, 'tipe' : Tipe})

def deletetipe(request,pk):
    Tipe = type_brg.objects.get(pk=pk)
    Tipe.delete()
    return redirect('/inventaris/masterdata/tipe')


