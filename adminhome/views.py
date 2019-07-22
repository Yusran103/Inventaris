from django.shortcuts import render, redirect
from adminhome.models import merk_brg , jenis_brg , supplier , type_brg , customer , barang_keluar, barang_masuk
from adminhome.forms import Merkform , Supplierform , Typeform, Jenisform, Customerform, BarangkeluarForm
from django.core.paginator import Paginator
from django.conf import settings
from django.core.files.storage import FileSystemStorage

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


def viewbarangkeluar(request):
    daftar_barangkeluar = barang_keluar.objects.all()
    pagination = Paginator(daftar_barangkeluar,5)

    page = request.GET.get('page','')
    barangkeluar_pg = pagination.get_page(page)
    return render(request, 'transaksi/keluar/view-barang-keluar.html', {'daftar_barangkeluar':barangkeluar_pg})


def barangkeluargrid(request):
    return render(request, 'transaksi/keluar/viewgrid-barang-keluar.html')


def editbarangkeluar(request):
    return render(request, 'transaksi/keluar/edit-barang-keluar.html')

def addbarangkeluar(request):
    daftar_merk = merk_brg.objects.all()
    daftar_tipe = type_brg.objects.all()
    daftar_jenis = jenis_brg.objects.all()
    daftar_customer = customer.objects.all()
    daftar_barangmasuk = barang_masuk.objects.all()

    if request.method == 'POST':
        form_data = request.POST
        form = BarangkeluarForm(form_data)
        if form.is_valid():
            Barangkeluar = barang_keluar(
                no_bukti=request.POST['no_bukti'],
                nm_brg_keluar=form.cleaned_data['value'],
                kd_brg_keluar=request.POST['kd_brg_keluar'],
                tgl_keluar=request.POST['tgl_keluar'],
                jml_keluar=request.POST['jml_keluar'],
                harga_satuan=request.POST['harga_satuan'],
                total_bayar=request.POST['total_bayar'],
                Costumer=request.POST['Customer'],
                alamat_customer=request.POST['alamat_customer'],
                no_resi=request.POST['no_resi'],
                merk_id=form.cleaned_data['value'],
                jenis_id=form.cleaned_data['value'],
                tipe_id=form.cleaned_data['value'],
                foto_keluar=request.FILES['foto_keluar'],
            )
            Barangkeluar.save()
            return redirect('/inventaris/transaksi/barangkeluar')
    else:
        form = BarangkeluarForm()
    return render(request, 'transaksi/keluar/add-barang-keluar.html', {'form':form, 'daftar_merk':daftar_merk, 'daftar_tipe':daftar_tipe, 'daftar_jenis':daftar_jenis, 'daftar_customer':daftar_customer, 'daftar_barangmasuk':daftar_barangmasuk})

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

def searchmerk(request):
    ''' This could be your actual view or a new one '''
    # Your code
    if request.method == 'GET': # If the form is submitted
        search_query = request.GET.get('search_box_merk', None)
        # Do whatever you need with the word the user looked for

    # Your code
def viewjenis(request):
    daftar_jenis = jenis_brg.objects.all()
    pagination = Paginator(daftar_jenis,5)

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


# Supplier
def viewsupplier(request):
    daftar_supplier = supplier.objects.all()
    pagination = Paginator(daftar_supplier,5)

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

# customer
def viewcustomer(request):
    daftar_customer = customer.objects.all()
    pagination = Paginator(daftar_customer,5)
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

def viewtipe(request):
    daftar_tipe = type_brg.objects.all()
    pagination = Paginator(daftar_tipe,5)

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
