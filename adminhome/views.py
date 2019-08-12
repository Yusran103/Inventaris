from django.shortcuts import render, get_object_or_404 ,redirect
from adminhome.models import Merk_brg , User , Jenis_brg , Supplier , Tipe_brg , Customer , Barang_masuk, Stok_barang, Barang_keluar
from adminhome.forms import Merkform , Customerform, Userform , Supplierform , Tipeform, Jenisform, Customerform ,Barang_masuk_form, Stok_form
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages, auth
from django.contrib import messages
from django.db import connection
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import bcrypt
from django.conf import settings
from django.template import context
from django.contrib.auth.hashers import make_password

# -----------+
# LOGIN      |
# -----------+

def index(request):
    return render(request, 'login.html')

def login_view(request):
    if request.POST:
        user = authenticate(username=request.POST['login_username'], password=request.POST['login_password'])
        if user is not None:
            akun = User.objects.get(id_user=user.id_user)
            login(request, user)
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

@login_required(login_url='/')
def cariuser(request):
    pengguna = request.GET.get('cari')
    daftar_user = User.objects.filter(
            Q(nm_lengkap__icontains=pengguna) | Q(username__icontains=pengguna) , Q(is_deleted='false')
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

@login_required(login_url='/')
def viewuser(request):
    daftar_user = User.objects.filter(is_deleted='false')
    adminonly = User.objects.filter(is_deleted='false',level='Admin')
    pagination = Paginator(daftar_user,10)
    page = request.GET.get('page','')
    user_pg = pagination.get_page(page)
    return render(request, 'users/view-user.html',{'daftar_users': user_pg,'adminonly':adminonly})

@login_required(login_url='/')
def register(request):
    url = '/inventaris/users/tambah'
    resp_body = '<script>alert("Username Sudah ada");\
            window.location="%s"</script>' % url
    if request.method == 'POST':
        form_data = request.POST
        form = Userform(form_data)
        cek = User.objects.filter(username=request.POST['username'])
        if cek == None:
            return HttpResponse(resp_body)
        else:
            if form.is_valid():
                akun = User(
                    nm_lengkap=request.POST['nm_lengkap'], 
                    email=request.POST['email'],
                    username=request.POST['username'], 
                    password=make_password(request.POST['password']),
                    level=request.POST['level'],
                    is_deleted='false'
                    )
                akun.save()
                messages.warning(request, 'Berhasil menambah %s'%(request.POST['nm_lengkap']))
                return redirect('/inventaris/users')
    else:
        form = Userform()
    return render(request, 'users/add-user.html', {'form': form,'messages':messages})

@login_required(login_url='/')
def edituser(request,pk):
    user = User.objects.get(pk=pk)
    if request.method == "POST":
        form = Userform(request.POST, instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            nm_lengkap = request.POST['nm_lengkap']
            email = request.POST['email']
            username = request.POST['username']
            level = request.POST['level']
            password = make_password(request.POST['password']),
            messages.warning(request, 'Berhasil merubah %s'%(user.nm_lengkap))
            user.save()
            return redirect('/inventaris/users', pk=user.pk)
    else:
        form = Userform(instance=user)
    return render(request, 'users/edit-user.html', {'form': form, 'user' : user,'messages':messages})

@login_required(login_url='/')
def deleteuser(request,pk):
    user = User.objects.get(pk=pk)
    messages.warning(request, 'Berhasil menghapus %s'%(user.nm_lengkap))
    cursor = connection.cursor()
    cursor.execute("update tb_user set is_deleted='True' where id_user='%s'"%(user.id_user))
    return redirect('/inventaris/users',{'messages':messages})

@login_required(login_url='/')
def changepassword(request,pk):
    user = User.objects.get(pk = request.session['id_user'])
    url = '/inventaris/'
    resp_body = '<script>alert("Password user %s Berhasil di rubah, Silahkan Login Kembali");\
            window.location="%s"</script>' % (user.nm_lengkap , url)

    if request.method == "POST":
        form = Userform(request.POST, instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            password = request.POST['password']
            user.save()
            return HttpResponse(resp_body)
    else:
        form = Userform(instance=user)
    return render(request, 'changepassword.html', {'form': form, 'user' : user,'messages':messages})

# -----------+
# DASHBOARD  |
# -----------+
@login_required(login_url='/')
def dashboard(request):
    Ssn = request.session
    if Ssn != None :
        for key, value in request.session.items():
            print('{} => {}'.format(key, value))
        return render(request, 'dashboard.html')
    else :
        return render(request, 'login.html')

# -----------+
# STOK       |
# -----------+
@login_required(login_url='/')
def caristokgrid(request):
    stok = request.GET.get('cari')
    daftar_barang = Stok_barang.objects.filter(
            Q(nm_barang__icontains=stok) | Q(kd_barang__icontains=stok)
        ).order_by('kd_barang', '-id_stok').distinct('kd_barang')
    pagination = Paginator(daftar_barang,5)
    page = request.GET.get('page')
    try:
        posts = pagination.page(page)
    except PageNotAnInteger:
        posts = pagination.page(1)
    except EmptyPage:
        posts = pagination.page(pagination.num_pages)
    
    context = {
        'daftar_stok': posts,
        'stok':stok
    }
    return render(request, 'transaksi/stok/viewgrid-stok.html', context)
@login_required(login_url='/')
def caristoklist(request):
    stok = request.GET.get('cari')
    daftar_barang = Stok_barang.objects.filter(
            Q(nm_barang__icontains=stok) | Q(kd_barang__icontains=stok)
        ).order_by('kd_barang', '-id_stok').distinct('kd_barang')
    pagination = Paginator(daftar_barang,10)
    page = request.GET.get('page')
    try:
        posts = pagination.page(page)
    except PageNotAnInteger:
        posts = pagination.page(1)
    except EmptyPage:
        posts = pagination.page(pagination.num_pages)
    
    context = {
        'daftar_stok': posts,
        'stok':stok
    }
    return render(request, 'transaksi/stok/view-stok.html', context)
@login_required(login_url='/')
def gridstok(request):
    daftar_stok = Stok_barang.objects.order_by('kd_barang', '-id_stok').distinct('kd_barang')
    pagination = Paginator(daftar_stok,5)

    page = request.GET.get('page','')
    barang_stok_pg = pagination.get_page(page)
    return render(request, 'transaksi/stok/viewgrid-stok.html', {'daftar_stok': barang_stok_pg})

@login_required(login_url='/')
def stok(request):
    daftar_stok = Stok_barang.objects.order_by('kd_barang', '-id_stok').distinct('kd_barang')
    pagination = Paginator(daftar_stok,10)

    page = request.GET.get('page','')
    barang_stok_pg = pagination.get_page(page)
    return render(request, 'transaksi/stok/view-stok.html', {'daftar_stok': barang_stok_pg})

# ------------+
# BARANG MASUK|
# ------------+
@login_required(login_url='/')
def caribarangmasukgrid(request):
    barangmasuk = request.GET.get('cari')
    daftar_barang = Barang_masuk.objects.filter(
            Q(nm_barang__icontains=barangmasuk) | Q(kd_barang__icontains=barangmasuk) |
            Q(sn_barang__icontains=barangmasuk) , Q(is_deleted='False')
        ).order_by('kd_barang')
    pagination = Paginator(daftar_barang,5)
    page = request.GET.get('page')
    try:
        posts = pagination.page(page)
    except PageNotAnInteger:
        posts = pagination.page(1)
    except EmptyPage:
        posts = pagination.page(pagination.num_pages)
    
    context = {
        'daftar_barang_masuk': posts,
        'barang_masuk':barangmasuk
    }
    return render(request, 'transaksi/masuk/viewgrid-barang-masuk.html', context)

@login_required(login_url='/')
def caribarangmasuk(request):
    barangmasuk = request.GET.get('cari')
    daftar_barang = Barang_masuk.objects.filter(
            Q(nm_barang__icontains=barangmasuk) | Q(kd_barang__icontains=barangmasuk) |
            Q(sn_barang__icontains=barangmasuk) , Q(is_deleted='False')
        ).order_by('kd_barang')
    pagination = Paginator(daftar_barang,10)
    page = request.GET.get('page')
    try:
        posts = pagination.page(page)
    except PageNotAnInteger:
        posts = pagination.page(1)
    except EmptyPage:
        posts = pagination.page(pagination.num_pages)
    
    context = {
        'daftar_barang_masuk': posts,
        'barang_masuk':barangmasuk
    }
    return render(request, 'transaksi/masuk/view-barang-masuk.html', context)

@login_required(login_url='/')
def barangmasuk(request):
    daftar_barang = Barang_masuk.objects.filter(is_deleted='False').order_by('-id_brg_masuk')
    pagination = Paginator(daftar_barang,10)

    page = request.GET.get('page','')
    barang_masuk_pg = pagination.get_page(page)
    return render(request, 'transaksi/masuk/view-barang-masuk.html', {'daftar_barang_masuk': barang_masuk_pg})

@login_required(login_url='/')
def barangmasukgrid(request):
    daftar_barang = Barang_masuk.objects.filter(is_deleted='False').order_by('-id_brg_masuk')
    pagination = Paginator(daftar_barang,5)

    page = request.GET.get('page','')
    barang_masuk_pg = pagination.get_page(page)
    return render(request, 'transaksi/masuk/viewgrid-barang-masuk.html', {'daftar_barang_masuk': barang_masuk_pg})

@login_required(login_url='/')
def editbarangmasuk(request,pk):
    masuk = Barang_masuk.objects.get(pk=pk)
    if request.method == "POST":
        form = Barang_masuk_form(request.POST,request.FILES, instance=masuk)
        if form.is_valid():
            barang_masuk = form.save(commit=False)
            kd_barang=request.POST['kd_barang'],
            nm_barang=request.POST['nm_barang'],
            sn_barang=request.POST['sn_barang'],
            tgl_masuk=request.POST['tgl_masuk'],
            harga_satuan=request.POST['harga_satuan'],
            supplier_id=Supplier.objects.get(pk=request.POST.get('supplier_id')),
            jml_masuk=request.POST['jml_masuk'],
            no_resi=request.POST['no_resi'],
            foto_masuk=request.FILES.get('foto_masuk'),
            jenis_id=Jenis_brg.objects.get(pk=request.POST.get('jenis_id')),
            merk_id=Merk_brg.objects.get(pk=request.POST.get('merk_id')),
            tipe_id=Tipe_brg.objects.get(pk=request.POST.get('tipe_id'))
            barang_masuk.save()

            # RAW UPDATE for STOK(LAST CHOICE)
            cursor = connection.cursor()
            cursor.execute(
                """update tb_stok set 
                    nm_barang='%s',
                    hrg_barang='%s',
                    jenis_id='%s',
                    merk_id='%s',
                    tipe_id='%s' where kd_barang='%s'"""
                    %(
                        request.POST['nm_barang'],
                        request.POST['harga_satuan'],
                        request.POST.get('jenis_id'),
                        request.POST.get('merk_id'),
                        request.POST.get('tipe_id'),
                        request.POST['kd_barang']
                    )
                )
            # CLEAR
            
            messages.success(request, 'Berhasil merubah %s'%(request.POST['nm_barang']))
            return redirect('/inventaris/barangmasuk', pk=masuk.pk)
    else:
        form = Barang_masuk_form(instance=masuk)
    return render(request, 'transaksi/masuk/edit-barang-masuk.html', {'form': form, 'barang_masuk' : masuk,'messages':messages})

@login_required(login_url='/')
def simpantambahbarangmasuk(request):
    jenis = Jenis_brg.objects.filter(is_deleted='False')
    merk = Merk_brg.objects.filter(is_deleted='False')
    tipe = Tipe_brg.objects.filter(is_deleted='False')
    supplier = Supplier.objects.filter(is_deleted='False')

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
                harga_satuan=request.POST['harga_satuan'],
                foto_masuk=request.FILES.get('foto_masuk'),
                jenis_id=Jenis_brg.objects.get(pk=request.POST.get('jenis_id')),
                merk_id=Merk_brg.objects.get(pk=request.POST.get('merk_id')),
                tipe_id=Tipe_brg.objects.get(pk=request.POST.get('tipe_id')),
                is_deleted='False'
            )
            form.save()
            
            if Stok_barang.objects.filter(kd_barang__icontains=request.POST.get('kd_barang')):
                # AMBIL DATA STOK AKHIR PALING BARU
                cr_stok = Stok_barang.objects.filter(kd_barang=request.POST.get('kd_barang')).latest('id_stok')
                stok_barang = Stok_barang.objects.create(
                    tanggal=request.POST['tgl_masuk'],
                    nm_barang=request.POST['nm_barang'],
                    kd_barang=request.POST['kd_barang'],
                    hrg_barang=request.POST['harga_satuan'],
                    jumlah_stok=request.POST['jml_masuk'],
                    stok_akhir= cr_stok.stok_akhir + int(request.POST['jml_masuk']),
                    keterangan="Barang Masuk",
                    foto_stok=request.FILES.get('foto_masuk'),
                    jenis_id=Jenis_brg.objects.get(pk=request.POST.get('jenis_id')),
                    merk_id=Merk_brg.objects.get(pk=request.POST.get('merk_id')),
                    tipe_id=Tipe_brg.objects.get(pk=request.POST.get('tipe_id'))
                )
            else:
                stok_barang = Stok_barang.objects.create(
                    tanggal=request.POST['tgl_masuk'],
                    nm_barang=request.POST['nm_barang'],
                    kd_barang=request.POST['kd_barang'],
                    hrg_barang=request.POST['harga_satuan'],
                    jumlah_stok=request.POST['jml_masuk'],
                    stok_akhir=request.POST['jml_masuk'],
                    keterangan="Barang Masuk",
                    foto_stok=request.FILES.get('foto_masuk'),
                    jenis_id=Jenis_brg.objects.get(pk=request.POST.get('jenis_id')),
                    merk_id=Merk_brg.objects.get(pk=request.POST.get('merk_id')),
                    tipe_id=Tipe_brg.objects.get(pk=request.POST.get('tipe_id'))
                )
            stok_barang.save()
            messages.success(request, 'Berhasil menambah %s'%(request.POST['nm_barang']))
            return redirect('/inventaris/barangmasuk/tambah')
    else:
        form = Barang_masuk_form()
    return render(request, 'transaksi/masuk/add-barang-masuk.html', 
    {
        'form': form,
        'daftar_jenis':jenis,
        'daftar_merk':merk,
        'daftar_tipe':tipe,
        'daftar_supplier':supplier,
        'messages':messages
    })

@login_required(login_url='/')
def tambahbarangmasuk(request):
    jenis = Jenis_brg.objects.filter(is_deleted='False')
    merk = Merk_brg.objects.filter(is_deleted='False')
    tipe = Tipe_brg.objects.filter(is_deleted='False')
    supplier = Supplier.objects.filter(is_deleted='False')
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
                harga_satuan=request.POST['harga_satuan'],
                foto_masuk=request.FILES.get('foto_masuk'),
                jenis_id=Jenis_brg.objects.get(pk=request.POST.get('jenis_id')),
                merk_id=Merk_brg.objects.get(pk=request.POST.get('merk_id')),
                tipe_id=Tipe_brg.objects.get(pk=request.POST.get('tipe_id')),
                is_deleted='False'
            )
            form.save()
            
            if Stok_barang.objects.filter(kd_barang__icontains=request.POST.get('kd_barang')):
                cr_stok = Stok_barang.objects.filter(kd_barang=request.POST.get('kd_barang')).latest('id_stok')
                stok_barang = Stok_barang.objects.create(
                    tanggal=request.POST['tgl_masuk'],
                    nm_barang=request.POST['nm_barang'],
                    kd_barang=request.POST['kd_barang'],
                    hrg_barang=request.POST['harga_satuan'],
                    jumlah_stok=request.POST['jml_masuk'],
                    stok_akhir= cr_stok.stok_akhir + int(request.POST['jml_masuk']),
                    keterangan="Barang Masuk",
                    foto_stok=request.FILES.get('foto_masuk'),
                    jenis_id=Jenis_brg.objects.get(pk=request.POST.get('jenis_id')),
                    merk_id=Merk_brg.objects.get(pk=request.POST.get('merk_id')),
                    tipe_id=Tipe_brg.objects.get(pk=request.POST.get('tipe_id'))
                )
            else:
                stok_barang = Stok_barang.objects.create(
                    tanggal=request.POST['tgl_masuk'],
                    nm_barang=request.POST['nm_barang'],
                    kd_barang=request.POST['kd_barang'],
                    hrg_barang=request.POST['harga_satuan'],
                    jumlah_stok=request.POST['jml_masuk'],
                    stok_akhir=request.POST['jml_masuk'],
                    keterangan="Barang Masuk",
                    foto_stok=request.FILES.get('foto_masuk'),
                    jenis_id=Jenis_brg.objects.get(pk=request.POST.get('jenis_id')),
                    merk_id=Merk_brg.objects.get(pk=request.POST.get('merk_id')),
                    tipe_id=Tipe_brg.objects.get(pk=request.POST.get('tipe_id'))
                )
            stok_barang.save()
            messages.success(request, 'Berhasil menambah %s'%(request.POST['nm_barang']))
            return redirect('/inventaris/barangmasuk/list')
    else:
        form = Barang_masuk_form()
    return render(request, 'transaksi/masuk/add-barang-masuk.html', 
    {
        'form': form,
        'daftar_jenis':jenis,
        'daftar_merk':merk,
        'daftar_tipe':tipe,
        'daftar_supplier':supplier,
        'messages':messages
    })

@login_required(login_url='/')
def deletebarangmasuk(request,pk):
    barang_masuk = Barang_masuk.objects.get(pk=pk)
    # stok = Barang_masuk.jml_masuk
    # jumlahstok = Stok_barang.objects.filter(kd_barang=barang_masuk.kd_barang).order_by('kd_barang', '-id_stok').distinct('kd_barang')
    if Stok_barang.objects.filter(kd_barang__icontains=barang_masuk.kd_barang):
        cr_stok = Stok_barang.objects.filter(kd_barang=barang_masuk.kd_barang).latest('id_stok')
        stok_barang = Stok_barang.objects.create(
            tanggal=barang_masuk.tgl_masuk,
            nm_barang=barang_masuk.nm_barang,
            kd_barang=barang_masuk.kd_barang,
            hrg_barang=barang_masuk.harga_satuan,
            jumlah_stok=barang_masuk.jml_masuk,
            stok_akhir= cr_stok.stok_akhir - int(barang_masuk.jml_masuk),
            keterangan="Hapus Barang Masuk",
            foto_stok=barang_masuk.foto_masuk,
            jenis_id=barang_masuk.jenis_id,
            merk_id=barang_masuk.merk_id,
            tipe_id=barang_masuk.tipe_id
        )   
        stok_barang.save()
    messages.success(request, 'Berhasil menghapus %s'%(barang_masuk.nm_barang))
    cursor = connection.cursor()
    cursor.execute("update tb_barang_masuk set is_deleted='True' where id_brg_masuk='%s'"%(barang_masuk.id_brg_masuk))
    return redirect('/inventaris/barangmasuk')

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
    barang_masuk = Stok_barang.objects.order_by('kd_barang', '-stok_akhir').distinct('kd_barang')
    jenis = Jenis_brg.objects.all()
    merk = Merk_brg.objects.all()
    tipe = Tipe_brg.objects.all()
    return render(request, 'transaksi/keluar/add-barang-keluar.html',{'masuk' : barang_masuk,'jenis':jenis,'merk':merk,'tipe':tipe})

# -------------+
# LAPORAN      |
# -------------+

@login_required(login_url='/')
def laporanmasuk(request):
    return render(request, 'laporan/laporan-barang-masuk.html')

@login_required(login_url='/')
def laporankeluar(request):
    return render(request, 'laporan/laporan-barang-keluar.html')

@login_required(login_url='/')
def laporanstok(request):
    return render(request, 'laporan/laporan-barang-stok.html')

@login_required(login_url='/')
def print_laporan_stok(request):
    judul = "Laporan Stok Barang"
    tanggal = request.POST.get('tanggal')
    url = '/inventaris/laporan/stok'
    resp_body = '<script>alert("Bulan di butuhkan");\
            window.location="%s"</script>' % url

    if tanggal == None:
        return HttpResponse(resp_body)
    else:
        pecah = tanggal.split('-')
        tahun = pecah[0]
        bulan = pecah[1]
    stok_barang = Stok_barang.objects.filter(tanggal__icontains=tanggal).order_by('tanggal')
    return render(request, 'laporan/print.html',{'stok':stok_barang,'tahun':tahun,'bulan':bulan,'judul':judul})

@login_required(login_url='/')
def print_laporan_masuk(request):
    judul = "Laporan Barang Masuk"
    tanggal = request.POST.get('tanggal')
    url = '/inventaris/laporan/barangmasuk'
    resp_body = '<script>alert("Bulan di butuhkan");\
            window.location="%s"</script>' % url

    if tanggal == None:
        return HttpResponse(resp_body)
    else:
        pecah = tanggal.split('-')
        tahun = pecah[0]
        bulan = pecah[1]
    stok_barang = Barang_masuk.objects.filter(tgl_masuk__icontains=tanggal,is_deleted='False').order_by('tgl_masuk')
    return render(request, 'laporan/print.html',{'stok':stok_barang,'tahun':tahun,'bulan':bulan,'judul':judul})

@login_required(login_url='/')
def print_laporan_keluar(request):
    judul = "Laporan Barang Keluar"
    tanggal = request.POST.get('tanggal')
    url = '/inventaris/laporan/barangkeluar'
    resp_body = '<script>alert("Bulan di butuhkan");\
            window.location="%s"</script>' % url

    if tanggal == None:
        return HttpResponse(resp_body)
    else:
        pecah = tanggal.split('-')
        tahun = pecah[0]
        bulan = pecah[1]
    stok_barang = Barang_keluar.objects.filter(tgl_keluar__icontains=tanggal,is_deleted='False').order_by('tgl_keluar')
    return render(request, 'laporan/print.html',{'stok':stok_barang,'tahun':tahun,'bulan':bulan,'judul':judul})

# -------------+
# MASTER DATA  |
# -------------+
# ------------+
#     MERK    |
# ------------+
@login_required(login_url='/')
def carimerk(request):
    merk = request.GET.get('cari')
    print(merk)
    daftar_merk = Merk_brg.objects.filter(
            nama_merk__icontains=merk,is_deleted='False'
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

@login_required(login_url='/')
def viewmerk(request):
    daftar_merk = Merk_brg.objects.filter(is_deleted='False').order_by('-id_merk')
    pagination = Paginator(daftar_merk,10)

    page = request.GET.get('page','')
    merk_pg = pagination.get_page(page)
    return render(request, 'masterdata/merk/merk.html', {'daftar_merk': merk_pg})

@login_required(login_url='/')
def addmerk(request):
    if request.method == 'POST':
        form_data = request.POST
        form = Merkform(form_data)
        if form.is_valid():
            Merk = Merk_brg(
                nama_merk=request.POST['nama_merk'],
                is_deleted='False'
            )
            Merk.save()
            messages.success(request, 'Berhasil menambah %s'%(request.POST['nama_merk']))
            return redirect('/inventaris/masterdata/merk')
    else:
        form = Merkform()
    return render(request, 'masterdata/merk/merk_tambah.html', {'form': form,'messages':messages})

@login_required(login_url='/')
def editmerk(request,pk):
    merk = Merk_brg.objects.get(pk=pk)
    if request.method == "POST":
        form = Merkform(request.POST, instance=merk)
        if form.is_valid():
            merk = form.save(commit=False)
            nama_merk = request.POST['nama_merk']
            merk.save()
            messages.success(request, 'Berhasil merubah %s'%(request.POST['nama_merk']))
            return redirect('/inventaris/masterdata/merk', pk=merk.pk)
    else:
        form = Merkform(instance=merk)
    return render(request, 'masterdata/merk/merk_edit.html', {'form': form, 'merk' : merk, 'messages':messages})

@login_required(login_url='/')
def deletemerk(request,pk):
    merk = Merk_brg.objects.get(pk=pk)
    messages.warning(request, 'Berhasil menghapus %s'%(merk.nama_merk))
    cursor = connection.cursor()
    cursor.execute("update tb_merk_brg set is_deleted='True' where id_merk='%s'"%(merk.id_merk))
    return redirect('/inventaris/masterdata/merk',{'messages':messages})

# ------------+
#     JENIS   |
# ------------+
@login_required(login_url='/')
def carijenis(request):
    jenis = request.GET.get('cari')
    daftar_jenis = Jenis_brg.objects.filter(
            nama_jenis__icontains=jenis,is_deleted='False'
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

@login_required(login_url='/')
def viewjenis(request):
    daftar_jenis = Jenis_brg.objects.filter(is_deleted='False').order_by('-id_jenis')
    pagination = Paginator(daftar_jenis,10)

    page = request.GET.get('page','')
    jenis_pg = pagination.get_page(page)
    return render(request, 'masterdata/jenis/jenis.html', {'daftar_jenis': jenis_pg})

@login_required(login_url='/')
def addjenis(request):
    if request.method == 'POST':
        form_data = request.POST
        form = Jenisform(form_data)
        if form.is_valid():
            jenis = Jenis_brg(
                nama_jenis=request.POST['nama_jenis'],
                is_deleted='False'
            )
            jenis.save()
            messages.success(request, 'Berhasil menambah %s'%(request.POST['nama_jenis']))
            return redirect('/inventaris/masterdata/jenis')
    else:
        form = Jenisform()
    return render(request, 'masterdata/jenis/jenis_tambah.html', {'form': form,'messages':messages})

@login_required(login_url='/')
def editjenis(request,pk):
    jenis = Jenis_brg.objects.get(pk=pk)
    if request.method == "POST":
        form = Jenisform(request.POST, instance=jenis)
        if form.is_valid():
            Jenis = form.save(commit=False)
            nama_jenis = request.POST['nama_jenis']
            Jenis.save()
            messages.success(request, 'Berhasil mengubah %s'%(request.POST['nama_jenis']))
            return redirect('/inventaris/masterdata/jenis', pk=jenis.pk)
    else:
        form = Jenisform(instance=jenis)
    return render(request, 'masterdata/jenis/jenis_edit.html', {'form': form, 'jenis' : jenis,'messages':messages})

@login_required(login_url='/')
def deletejenis(request,pk):
    jenis = Jenis_brg.objects.get(pk=pk)
    # RAW (LAST CHOICE)
    cursor = connection.cursor()
    cursor.execute("update tb_jenis_brg set is_deleted='True' where id_jenis='%s'"%(jenis.id_jenis))

    messages.success(request, 'Berhasil menghapus %s'%(jenis.nama_jenis))
    return redirect('/inventaris/masterdata/jenis',{'messages':messages})

# -------------+
#    SUPPLIER  |
# -------------+
@login_required(login_url='/')
def carisuplier(request):
    suplier = request.GET.get('cari')
    daftar_supplier = Supplier.objects.filter(
            Q(nama_supplier__icontains=suplier) | Q(alamat_supplier__icontains=suplier) |
            Q(notlp_supplier__icontains=suplier) , Q(is_deleted='False')
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

@login_required(login_url='/')
def viewsupplier(request):
    daftar_supplier = Supplier.objects.filter(is_deleted='False').order_by('-id_supplier')
    pagination = Paginator(daftar_supplier,10)

    page = request.GET.get('page','')
    supplier_pg = pagination.get_page(page)
    return render(request, 'masterdata/supplier/supplier.html', {'daftar_supplier': supplier_pg})

@login_required(login_url='/')
def addsupplier(request):
    if request.method == 'POST':
        form_data = request.POST
        form = Supplierform(form_data)
        if form.is_valid():
            supplier = Supplier(
                nama_supplier=request.POST['nama_supplier'],
                alamat_supplier=request.POST['alamat_supplier'],
                notlp_supplier=request.POST['notlp_supplier'],
                is_deleted='False'
            )
            supplier.save()
            messages.success(request, 'Berhasil menambah %s'%(request.POST['nama_supplier']))
            return redirect('/inventaris/masterdata/supplier')
    else:
        form = Supplierform()
    return render(request, 'masterdata/supplier/supplier_tambah.html', {'form': form,'messages':messages})

@login_required(login_url='/')
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
            messages.success(request, 'Berhasil merubah %s'%(request.POST['nama_supplier']))
            return redirect('/inventaris/masterdata/supplier', pk=supplier.pk)
    else:
        form = Supplierform(instance=supplier)
    return render(request, 'masterdata/supplier/supplier_edit.html', {'form': form, 'supplier' : supplier,'messages':messages})

@login_required(login_url='/')
def deletesupplier(request,pk):
    supplier = Supplier.objects.get(pk=pk)
    messages.success(request, 'Berhasil menghapus %s'%(supplier.nama_supplier))
    
    cursor = connection.cursor()
    cursor.execute("update tb_supplier set is_deleted='True' where id_supplier='%s'"%(supplier.id_supplier))
    
    return redirect('/inventaris/masterdata/supplier',{'messages':messages})

# -------------+
#    CUSTOMER  |
# -------------+

@login_required(login_url='/')
def caricustomer(request):
    customers = request.GET.get('cari')
    daftar_customer = Customer.objects.filter(
            Q(nama_customer__icontains=customers) | Q(alamat_customer__icontains=customers) |
            Q(notlp_customer__icontains=customers) , Q(is_deleted='False')
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

@login_required(login_url='/')
def viewcustomer(request):
    daftar_customer = Customer.objects.filter(is_deleted='False').order_by('-id_customer')
    pagination = Paginator(daftar_customer,10)
    page = request.GET.get('page','')
    customer_pg = pagination.get_page(page)
    return render(request, 'masterdata/customer/customer.html',{'daftar_customer': customer_pg})

@login_required(login_url='/')
def addcustomer(request):
    if request.method == 'POST':
        form_data = request.POST
        form = Customerform(form_data)
        if form.is_valid():
            customer = Customer(
                nama_customer= request.POST['nama_customer'],
                alamat_customer=request.POST['alamat_customer'],
                notlp_customer=request.POST['notlp_customer'],
                is_deleted='False'
            )
            messages.success(request, 'Berhasil menambah %s'%(request.POST['nama_customer']))
            customer.save()
            return redirect('/inventaris/masterdata/customer')
    else:
        form = Customerform()
    return render(request, 'masterdata/customer/customer_tambah.html', {'form': form,'messages':messages})

@login_required(login_url='/')
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
            messages.success(request, 'Berhasil merubah %s'%(request.POST['nama_customer']))
            return redirect('/inventaris/masterdata/customer', pk=customer.pk)
    else:
        form = Customerform(instance=customer)
    return render(request, 'masterdata/customer/customer_edit.html', {'form': form, 'customer' : customer,'messages':messages})

@login_required(login_url='/')
def deletecustomer(request,pk):
    customer = Customer.objects.get(pk=pk)
    messages.success(request, 'Berhasil menghapus %s'%(customer.nama_customer))
    
    cursor = connection.cursor()
    cursor.execute("update tb_customer set is_deleted='True' where id_customer='%s'"%(customer.id_customer))
    
    return redirect('/inventaris/masterdata/customer',{'messages':messages})

# -------------+
#    TIPE      |
# -------------+

@login_required(login_url='/')
def caritipe(request):
    tipe = request.GET.get('cari')
    daftar_tipe = Tipe_brg.objects.filter(
            nama_tipe__icontains=tipe,is_deleted='False'
        ).order_by('nama_tipe')
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

@login_required(login_url='/')
def viewtipe(request):
    daftar_tipe = Tipe_brg.objects.filter(is_deleted='False').order_by('-id_tipe')
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
                nama_tipe=request.POST['nama_tipe'],
                is_deleted='False'
            )
            Tipe.save()
            messages.success(request, 'Berhasil menambah %s'%(request.POST['nama_tipe']))
            return redirect('/inventaris/masterdata/tipe')
    else:
        form = Tipeform()
    return render(request, 'masterdata/tipe/tipe_tambah.html', {'form': form,'messages':messages})

@login_required(login_url='/')
def edittipe(request,pk):
    tipe = Tipe_brg.objects.get(pk=pk)
    if request.method == "POST":
        form = Tipeform(request.POST, instance=tipe)
        if form.is_valid():
            Tipe = form.save(commit=False)
            nama_tipe= request.POST['nama_tipe']
            Tipe.save()
            messages.success(request, 'Berhasil merubah %s'%(request.POST['nama_tipe']))
            return redirect('/inventaris/masterdata/tipe', pk=tipe.pk)
    else:
        form = Tipeform(instance=tipe)
    return render(request, 'masterdata/tipe/tipe_edit.html', {'form': form, 'tipe' : tipe,'messages':messages})

@login_required(login_url='/')
def deletetipe(request,pk):
    tipe = Tipe_brg.objects.get(pk=pk)
    messages.success(request, 'Berhasil menghapus %s'%(tipe.nama_tipe))
    cursor = connection.cursor()
    cursor.execute("update tb_tipe_brg set is_deleted='True' where id_tipe='%s'"%(tipe.id_tipe))
    return redirect('/inventaris/masterdata/tipe',{'messages':messages})
