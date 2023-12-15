from django.contrib import admin
from . models import product
class productAdmin(admin.ModelAdmin):
    list_display = ('name','price','stock','image')

# Register your models here.

admin.site.register(product,productAdmin)
