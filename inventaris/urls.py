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
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
from adminhome import views as adminhome


urlpatterns = [
    path('admin/', admin.site.urls),
    # LOGIN FROM
    path('', adminhome.index, name='login'),
    # FORGET PASSWORD
    path('changepassword/', adminhome.changepassword, name='changepassword'),
    # ADMIN DASHBOARD
    path('inventaris/', adminhome.dashboard, name='dashboard'),
    # BARANG MASUK
    path('inventaris/barangmasuk',adminhome.barangmasukgrid, name='barangmasuk_grid'),
    path('inventaris/barangmasuk/list',adminhome.barangmasuk, name='barangmasuk_list'),
    path('inventaris/barangmasuk/tambah',adminhome.tambahbarangmasuk, name='barangmasuk_add'),
    # path('inventaris/barangmasuk/edit/<id:pk>', adminhome.editbarangmasuk,name='barangmasuk_edit'),
    # path('inventaris/barangmasuk/delete/<id:pk>', adminhome.editbarangmasuk,name='barangmasuk_delete'),

    # BARANG KELUAR
    path('inventaris/barangkeluar',adminhome.barangkeluargrid, name='barangkeluar_grid'),
    path('inventaris/barangkeluar/list',adminhome.viewbarangkeluar, name='barangkeluar_list'),
    path('inventaris/barangkeluar/tambah',adminhome.addbarangkeluar, name='barangkeluar_add'),
    # path('inventaris/barangkeluar/edit/<id:pk>', adminhome.editbarangkeluar,name='barangkeluar_edit'),
    # path('inventaris/barangkeluar/delete/<id:pk>', adminhome.editbarangkeluar,name='barangkeluar_delete'),    
    
    # STOK
    path('inventaris/stok', adminhome.gridstok, name='stok_grid'),
    path('inventaris/stok/list', adminhome.stok, name='stok_list'),
    
    # LAPORAN
    path('inventaris/laporan/barangmasuk',adminhome.laporanmasuk, name='laporan_masuk'),
    path('inventaris/laporan/barangkeluar',adminhome.laporankeluar, name='laporan_keluar'),
    path('inventaris/laporan/stok', adminhome.laporanstok, name='laporan_stok'),
    
    # USERS
    path('inventaris/users', adminhome.viewuser, name='user'),
    path('inventaris/users/tambah', adminhome.adduser, name='user_add'),
    path('inventaris/users/edit', adminhome.edituser, name='user_edit'),
    
    # MASTERDATA
    # MERK
    path('inventaris/masterdata/merk', adminhome.viewmerk, name='merk'),
    path('inventaris/masterdata/merk/tambah',adminhome.addmerk, name='merk_add'),
    path('inventaris/masterdata/merk/edit/<int:pk>', adminhome.editmerk,name='merk_edit'),
    path('inventaris/masterdata/merk/delete/<int:pk>', adminhome.deletemerk,name='merk_delete'),
    
    # JENIS
    path('inventaris/masterdata/jenis', adminhome.viewjenis, name='jenis'),
    path('inventaris/masterdata/jenis/tambah',adminhome.addjenis, name='jenis_add'),
    path('inventaris/masterdata/jenis/edit/<int:pk>', adminhome.editjenis,name='jenis_edit'),
    path('inventaris/masterdata/jenis/delete/<int:pk>', adminhome.deletejenis,name='jenis_delete'),
    
    # SUPPLIER 
    path('inventaris/masterdata/supplier', adminhome.viewsupplier, name='supplier'),
    path('inventaris/masterdata/supplier/tambah',adminhome.addsupplier, name='supplier_add'),
    path('inventaris/masterdata/supplier/edit/<int:pk>', adminhome.editsupplier,name='supplier_edit'),
    path('inventaris/masterdata/supplier/delete/<int:pk>', adminhome.deletesupplier,name='merk_delete'),
    
    # CUSTOMER
    path('inventaris/masterdata/customer', adminhome.viewcustomer, name='customer'),
    path('inventaris/masterdata/customer/tambah',adminhome.addcustomer, name='customer_add'),
    path('inventaris/masterdata/customer/edit/<int:pk>', adminhome.editcustomer,name='customer_edit'),
    path('inventaris/masterdata/customer/delete/<int:pk>', adminhome.deletecustomer,name='customer_delete'),
    
    # TIPE
    path('inventaris/masterdata/tipe', adminhome.viewtipe, name='tipe'),
    path('inventaris/masterdata/tipe/tambah',adminhome.addtipe, name='tipe_add'),
    path('inventaris/masterdata/tipe/edit/<int:pk>', adminhome.edittipe,name='tipe_edit'),
    path('inventaris/masterdata/tipe/delete/<int:pk>', adminhome.deletetipe,name='tipe_delete'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
