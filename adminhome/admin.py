from django.contrib import admin

# Register your models here.
from adminhome.models import User
from adminhome.forms import Userform

class UserAdmin(admin.ModelAdmin):
    form = Userform

admin.site.register(User,UserAdmin)