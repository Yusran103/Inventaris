from django.shortcuts import render, get_object_or_404 ,redirect
from adminhome.models import Merk_brg , Jenis_brg , Supplier , Tipe_brg , Customer , Barang_masuk
from adminhome.forms import Merkform , Supplierform , Tipeform, Jenisform, Customerform ,Barang_masuk_form
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
    daftar_barang = Barang_masuk.objects.all()
    pagination = Paginator(daftar_barang,10)

    page = request.GET.get('page','')
    barang_masuk_pg = pagination.get_page(page)
    return render(request, 'transaksi/masuk/view-barang-masuk.html', {'daftar_barang_masuk': barang_masuk_pg})


def barangmasukgrid(request):
    daftar_barang = Barang_masuk.objects.all()
    pagination = Paginator(daftar_barang,10)

    page = request.GET.get('page','')
    barang_masuk_pg = pagination.get_page(page)
    return render(request, 'transaksi/masuk/viewgrid-barang-masuk.html', {'daftar_barang_masuk': barang_masuk_pg})


def editbarangmasuk(request,pk):
    barang_masuk = Barang_masuk.objects.get(pk=pk)
    if request.method == "POST":
        form = Merkform(request.POST, instance=barang_masuk)
        if form.is_valid():
            barang_masuk = form.save(commit=False)
            nama_merk = request.POST['nama_merk']
            barang_masuk.save()
            return redirect('/inventaris/masterdata/merk', pk=barang_masuk.pk)
    else:
        form = Merkform(instance=barang_masuk)
    return render(request, 'transaksi/masuk/edit-barang-masuk.html', {'form': form, 'barang_masuk' : barang_masuk})


def tambahbarangmasuk(request):
    jenis = Jenis_brg.objects.all()
    merk = Merk_brg.objects.all()
    tipe = Tipe_brg.objects.all()
    supplier = Supplier.objects.all()

    if request.method == 'POST':
        form = Barang_masuk_form(request.POST , request.FILES)
        if form.is_valid():
            form = Barang_masuk(
                kd_barang=request.POST['kd_barang'],
                nm_barang=request.POST['nm_barang'],
                sn_barang=request.POST['sn_barang'],
                tgl_masuk=request.POST['tgl_masuk'],
                supplier_id=Supplier.objects.get(pk=request.POST.get('supplier_id')),
                jml_masuk=request.POST['jml_masuk'],
                no_resi=request.POST['no_resi'],
                foto_masuk=request.FILES['foto_masuk'],
                jenis_id=Jenis_brg.objects.get(pk=request.POST.get('jenis_id')),
                merk_id=Merk_brg.objects.get(pk=request.POST.get('merk_id')),
                tipe_id=Tipe_brg.objects.get(pk=request.POST.get('tipe_id'))
            )
            form.save()
            return redirect('/inventaris/barangmasuk/list')
    else:
        form = Barang_masuk_form()
    return render(request, 'transaksi/masuk/add-barang-masuk.html', 
    {
        'form': form,
        'daftar_jenis':jenis,
        'daftar_merk':merk,
        'daftar_tipe':tipe,
        'daftar_supplier':supplier
        })

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
    daftar_merk = Merk_brg.objects.all()
    pagination = Paginator(daftar_merk,10)

    page = request.GET.get('page','')
    merk_pg = pagination.get_page(page)
    return render(request, 'masterdata/merk/merk.html', {'daftar_merk': merk_pg})


def addmerk(request):
    if request.method == 'POST':
        form_data = request.POST
        form = Merkform(form_data)
        if form.is_valid():
            Merk = Merk_brg(
                nama_merk=request.POST['nama_merk']
            )
            Merk.save()
            return redirect('/inventaris/masterdata/merk')
    else:
        form = Merkform()
    return render(request, 'masterdata/merk/merk_tambah.html', {'form': form})


def editmerk(request,pk):
    merk = Merk_brg.objects.get(pk=pk)
    if request.method == "POST":
        form = Merkform(request.POST, instance=merk)
        if form.is_valid():
            merk = form.save(commit=False)
            nama_merk = request.POST['nama_merk']
            merk.save()
            return redirect('/inventaris/masterdata/merk', pk=merk.pk)
    else:
        form = Merkform(instance=merk)
    return render(request, 'masterdata/merk/merk_edit.html', {'form': form, 'merk' : merk})

def deletemerk(request,pk):
    Merk = Merk_brg.objects.get(pk=pk)
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
    daftar_jenis = Jenis_brg.objects.all()
    pagination = Paginator(daftar_jenis,10)

    page = request.GET.get('page','')
    jenis_pg = pagination.get_page(page)
    return render(request, 'masterdata/jenis/jenis.html', {'daftar_jenis': jenis_pg})

def addjenis(request):
    if request.method == 'POST':
        form_data = request.POST
        form = Jenisform(form_data)
        if form.is_valid():
            jenis = Jenis_brg(
                nama_jenis=request.POST['nama_jenis']
            )
            jenis.save()
            return redirect('/inventaris/masterdata/jenis')
    else:
        form = Jenisform()
    return render(request, 'masterdata/jenis/jenis_tambah.html', {'form': form})

def editjenis(request,pk):
    jenis = Jenis_brg.objects.get(pk=pk)
    if request.method == "POST":
        form = Jenisform(request.POST, instance=jenis)
        if form.is_valid():
            Jenis = form.save(commit=False)
            nama_jenis = request.POST['nama_jenis']
            Jenis.save()
            return redirect('/inventaris/masterdata/jenis', pk=jenis.pk)
    else:
        form = Jenisform(instance=jenis)
    return render(request, 'masterdata/jenis/jenis_edit.html', {'form': form, 'jenis' : jenis})

def deletejenis(request,pk):
    jenis = Jenis_brg.objects.get(pk=pk)
    jenis.delete()
    return redirect('/inventaris/masterdata/jenis')

def viewsupplier(request):
    daftar_supplier = Supplier.objects.all()
    pagination = Paginator(daftar_supplier,10)

    page = request.GET.get('page','')
    supplier_pg = pagination.get_page(page)
    return render(request, 'masterdata/supplier/supplier.html', {'daftar_supplier': supplier_pg})

def addsupplier(request):
    if request.method == 'POST':
        form_data = request.POST
        form = Supplierform(form_data)
        if form.is_valid():
            supplier = Supplier(
                nama_supplier=request.POST['nama_supplier'],
                alamat_supplier=request.POST['alamat_supplier'],
                notlp_supplier=request.POST['notlp_supplier']
            )
            supplier.save()
            return redirect('/inventaris/masterdata/supplier')
    else:
        form = Supplierform()
    return render(request, 'masterdata/supplier/supplier_tambah.html', {'form': form})

def editsupplier(request,pk):
    supplier = Supplier.objects.get(pk=pk)
    if request.method == "POST":
        form = Supplierform(request.POST, instance=Supplier)
        if form.is_valid():
            supplier = form.save(commit=False)
            nama_supplier = request.POST['nama_supplier']
            alamat_supplier = request.POST['alamat_supplier']
            notlp_supplier = request.POST['notlp_supplier']
            supplier.save()
            return redirect('/inventaris/masterdata/supplier', pk=supplier.pk)
    else:
        form = Supplierform(instance=supplier)
    return render(request, 'masterdata/supplier/supplier_edit.html', {'form': form, 'supplier' : supplier})

def deletesupplier(request,pk):
    supplier = Supplier.objects.get(pk=pk)
    supplier.delete()
    return redirect('/inventaris/masterdata/supplier')

def viewcustomer(request):
    daftar_customer = Customer.objects.all()
    pagination = Paginator(daftar_customer,10)
    page = request.GET.get('page','')
    customer_pg = pagination.get_page(page)
    return render(request, 'masterdata/customer/customer.html',{'daftar_customer': customer_pg})

def addcustomer(request):
    if request.method == 'POST':
        form_data = request.POST
        form = Customerform(form_data)
        if form.is_valid():
            customer = Customer(
                nama_customer= request.POST['nama_customer'],
                alamat_customer=request.POST['alamat_customer'],
                notlp_customer=request.POST['notlp_customer']
            )
            customer.save()
            return redirect('/inventaris/masterdata/customer')
    else:
        form = Customerform()
    return render(request, 'masterdata/customer/customer_tambah.html', {'form': form})

def editcustomer(request,pk):
    customer = Customer.objects.get(pk=pk)
    if request.method == "POST":
        form = Customerform(request.POST, instance=customer)
        if form.is_valid():
            customer = form.save(commit=False)
            nama_customer = request.POST['nama_customer']
            alamat_customer = request.POST['alamat_customer']
            notlp_customer = request.POST['notlp_customer']
            customer.save()
            return redirect('/inventaris/masterdata/customer', pk=customer.pk)
    else:
        form = Customerform(instance=customer)
    return render(request, 'masterdata/customer/customer_edit.html', {'form': form, 'customer' : customer})

def deletecustomer(request,pk):
    customer = Customer.objects.get(pk=pk)
    customer.delete()
    return redirect('/inventaris/masterdata/customer')

def viewtipe(request):
    daftar_tipe = Tipe_brg.objects.all()
    pagination = Paginator(daftar_tipe,10)

    page = request.GET.get('page','')
    tipe_pg = pagination.get_page(page)
    return render(request, 'masterdata/tipe/tipe.html',{'daftar_tipe': tipe_pg})

def addtipe(request):
    if request.method == 'POST':
        form_data = request.POST
        form = Tipeform(form_data)
        if form.is_valid():
            Tipe = Tipe_brg(
                nama_tipe=request.POST['nama_tipe']
            )
            Tipe.save()
            return redirect('/inventaris/masterdata/tipe')
    else:
        form = Tipeform()
    return render(request, 'masterdata/tipe/tipe_tambah.html', {'form': form})

def edittipe(request,pk):
    tipe = Tipe_brg.objects.get(pk=pk)
    if request.method == "POST":
        form = Tipeform(request.POST, instance=tipe)
        if form.is_valid():
            Tipe = form.save(commit=False)
            nama_tipe= request.POST['nama_tipe']
            Tipe.save()
            return redirect('/inventaris/masterdata/tipe', pk=tipe.pk)
    else:
        form = Tipeform(instance=Tipe)
    return render(request, 'masterdata/tipe/tipe_edit.html', {'form': form, 'tipe' : tipe})

def deletetipe(request,pk):
    tipe = Tipe_brg.objects.get(pk=pk)
    tipe.delete()
    return redirect('/inventaris/masterdata/tipe')
