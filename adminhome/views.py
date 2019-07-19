from django.shortcuts import render, redirect
from adminhome.models import merk_brg, jenis_brg
from adminhome.forms import Merkform
from django.core.paginator import Paginator

# -----------+
# LOGIN      |
# -----------+

def index(request):
    return render(request, 'login.html')

# -----------+
# DASHBOARD  |
# -----------+


def dashboard(request):
    return render(request, 'dashboard.html')

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

# -------------+
# USERS        |
# -------------+


def viewuser(request):
    return render(request, 'users/view-user.html')


def adduser(request):
    return render(request, 'users/add-user.html')


def edituser(request):
    return render(request, 'users/edit-user.html')

# ---------------+
# CHANGE PASSWORD|
# ---------------+


def changepassword(request):
    return render(request, 'changepassword.html')

# -------------+
# MASTER DATA  |
# -------------+


def viewmerk(request):
    daftar_merk = merk_brg.objects.all()
    pagination = Paginator(daftar_merk,5)

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
    return render(request, 'masterdata/merk/merk_edit.html')

def deletemerk(request,pk):
    Merk = merk_brg.objects.get(pk=pk)
    Merk.delete()
    return redirect('/inventaris/masterdata/merk')

def viewjenis(request):
    return render(request, 'masterdata/jenis/jenis.html')

def addjenis(request):
    return render(request, 'masterdata/jenis/jenis_tambah.html')

def editjenis(request):
    return render(request, 'masterdata/jenis/jenis_edit.html')

def viewsupplier(request):
    return render(request, 'masterdata/supplier/supplier.html')

def addsupplier(request):
    return render(request, 'masterdata/supplier/supplier_tambah.html')

def editsupplier(request):
    return render(request, 'masterdata/supplier/supplier_edit.html')

def viewcustomer(request):
    return render(request, 'masterdata/customer/customer.html')

def addcustomer(request):
    return render(request, 'masterdata/customer/customer_tambah.html')

def editcustomer(request):
    return render(request, 'masterdata/customer/customer_edit.html')

def viewtipe(request):
    return render(request, 'masterdata/tipe/tipe.html')

def addtipe(request):
    return render(request, 'masterdata/tipe/tipe_tambah.html')

def edittipe(request):
    return render(request, 'masterdata/tipe/tipe_edit.html')
