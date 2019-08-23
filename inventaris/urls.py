"""inventaris URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from adminhome import views as adminhome


urlpatterns = [
    path('admin/', admin.site.urls),
    # LOGIN FROM
    path('', adminhome.index, name='login'),
    path('inventaris/logout', adminhome.logout_view, name='logout'),
    path('register', adminhome.register, name='regis'),
    path('login', adminhome.login_view, name='login_view'),
    # FORGET PASSWORD
    path('changepassword/<int:pk>', adminhome.changepassword, name='changepassword'),
    # ADMIN DASHBOARD
    path('inventaris/', adminhome.dashboard, name='dashboard'),
    # BARANG MASUK
    path('inventaris/barangmasuk',adminhome.barangmasukgrid, name='barangmasuk_grid'),
    path('inventaris/barangmasuk/list',adminhome.barangmasuk, name='barangmasuk_list'),
    path('inventaris/barangmasuk/tambah',adminhome.tambahbarangmasuk, name='barangmasuk_add'),
    path('inventaris/barangmasuk/simpantambah',adminhome.simpantambahbarangmasuk, name='barangmasuk_addcreate'),
    path('inventaris/barangmasuk/edit/<int:pk>', adminhome.editbarangmasuk,name='barangmasuk_edit'),
    path('inventaris/barangmasuk/delete/<int:pk>', adminhome.deletebarangmasuk,name='barangmasuk_delete'),
    path('inventaris/barangmasuk/cari', adminhome.caribarangmasukgrid,name='barangmasuk_grid_cari'),
    path('inventaris/barangmasuk/list/cari', adminhome.caribarangmasuk,name='barangmasuk_cari'),

    # BARANG KELUAR
    path('inventaris/barangkeluar',adminhome.barangkeluargrid, name='barangkeluar_grid'),
    path('inventaris/barangkeluar/list',adminhome.viewbarangkeluar, name='barangkeluar_list'),
    path('inventaris/barangkeluar/tambah',adminhome.addbarangkeluar, name='barangkeluar_add'),
    path('inventaris/barangkeluar/simpantambah',adminhome.simpantambahbarangkeluar, name='barangkeluar_addcreate'),
    path('inventaris/barangkeluar/edit/<int:pk>', adminhome.editbarangkeluar,name='barangkeluar_edit'),
    path('inventaris/barangkeluar/delete/<int:pk>', adminhome.deletebarangkeluar,name='barangkeluar_delete'),
    path('inventaris/barangkeluar/cari', adminhome.caribarangkeluargrid,name='barangkeluar_grid_cari'),
    path('inventaris/barangkeluar/list/cari', adminhome.caribarangkeluar,name='barangkeluar_cari'),

    # BARANG RETUR
    path('inventaris/barangretur',adminhome.barangreturgrid, name='barangretur_grid'),
    path('inventaris/barangretur/list',adminhome.barangretur, name='barangretur_list'),
    path('inventaris/barangretur/tambah',adminhome.tambahbarangretur, name='barangretur_add'),
    path('inventaris/barangretur/simpantambah',adminhome.simpantambahbarangretur, name='barangretur_addcreate'),
    path('inventaris/barangretur/edit/<int:pk>', adminhome.editbarangretur,name='barangretur_edit'),
    path('inventaris/barangretur/delete/<int:pk>', adminhome.deletebarangretur,name='barangretur_delete'),
    path('inventaris/barangretur/cari', adminhome.caribarangreturgrid,name='barangretur_grid_cari'),
    path('inventaris/barangretur/list/cari', adminhome.caribarangretur,name='barangretur_cari'),

    # STOK
    path('inventaris/stok', adminhome.gridstok, name='stok_grid'),
    path('inventaris/stok/cari', adminhome.caristokgrid, name='stok_grid_cari'),
    path('inventaris/stok/list/cari', adminhome.caristoklist, name='stok_cari'),
    path('inventaris/stok/list', adminhome.stok, name='stok_list'),
    
    # LAPORAN
    path('inventaris/laporan/barangmasuk',adminhome.laporanmasuk, name='laporan_masuk'),
    path('inventaris/laporan/barangkeluar',adminhome.laporankeluar, name='laporan_keluar'),
    path('inventaris/laporan/stok', adminhome.laporanstok, name='laporan_stok'),
    path('inventaris/laporan/print/stok', adminhome.print_laporan_stok, name='print_stok'),
    path('inventaris/laporan/print/masuk', adminhome.print_laporan_masuk, name='print_masuk'),
    path('inventaris/laporan/print/keluar', adminhome.print_laporan_keluar, name='print_keluar'),
    # CETAK INVOICE
    path('invoice/', adminhome.invoice, name='invoice'),
    path('invoice/print', adminhome.print_invoice, name='print_invoice'),
    
    # USERS
    path('inventaris/users', adminhome.viewuser, name='user'),
    path('inventaris/users/tambah', adminhome.register, name='user_add'),
    path('inventaris/users/edit/<int:pk>', adminhome.edituser, name='user_edit'),
    path('inventaris/users/delete/<int:pk>', adminhome.deleteuser,name='user_delete'),
    path('inventaris/users/cari', adminhome.cariuser,name='user_cari'),
    
    # MASTERDATA
    # MERK
    path('inventaris/masterdata/merk', adminhome.viewmerk, name='merk'),
    path('inventaris/masterdata/merk/tambah',adminhome.addmerk, name='merk_add'),
    path('inventaris/masterdata/merk/edit/<int:pk>', adminhome.editmerk,name='merk_edit'),
    path('inventaris/masterdata/merk/delete/<int:pk>', adminhome.deletemerk,name='merk_delete'),
    path('inventaris/masterdata/merk/cari', adminhome.carimerk,name='merk_cari'),
    
    # JENIS
    path('inventaris/masterdata/jenis', adminhome.viewjenis, name='jenis'),
    path('inventaris/masterdata/jenis/tambah',adminhome.addjenis, name='jenis_add'),
    path('inventaris/masterdata/jenis/edit/<int:pk>', adminhome.editjenis,name='jenis_edit'),
    path('inventaris/masterdata/jenis/delete/<int:pk>', adminhome.deletejenis,name='jenis_delete'),
    path('inventaris/masterdata/jenis/cari', adminhome.carijenis,name='jenis_cari'),
    
    # SUPPLIER 
    path('inventaris/masterdata/supplier', adminhome.viewsupplier, name='supplier'),
    path('inventaris/masterdata/supplier/tambah',adminhome.addsupplier, name='supplier_add'),
    path('inventaris/masterdata/supplier/edit/<int:pk>', adminhome.editsupplier,name='supplier_edit'),
    path('inventaris/masterdata/supplier/delete/<int:pk>', adminhome.deletesupplier,name='supplier_delete'),
    path('inventaris/masterdata/supplier/cari', adminhome.carisuplier,name='supplier_cari'),
    
    # CUSTOMER
    path('inventaris/masterdata/customer', adminhome.viewcustomer, name='customer'),
    path('inventaris/masterdata/customer/tambah',adminhome.addcustomer, name='customer_add'),
    path('inventaris/masterdata/customer/edit/<int:pk>', adminhome.editcustomer,name='customer_edit'),
    path('inventaris/masterdata/customer/delete/<int:pk>', adminhome.deletecustomer,name='customer_delete'),
    path('inventaris/masterdata/customer/cari', adminhome.caricustomer,name='customer_cari'),
    
    # TIPE
    path('inventaris/masterdata/tipe', adminhome.viewtipe, name='tipe'),
    path('inventaris/masterdata/tipe/tambah',adminhome.addtipe, name='tipe_add'),
    path('inventaris/masterdata/tipe/edit/<int:pk>', adminhome.edittipe,name='tipe_edit'),
    path('inventaris/masterdata/tipe/delete/<int:pk>', adminhome.deletetipe,name='tipe_delete'),
    path('inventaris/masterdata/tipe/cari', adminhome.caritipe,name='tipe_cari'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
