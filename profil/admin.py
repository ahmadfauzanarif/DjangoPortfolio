from django.contrib import admin

from .models import Barang, Jenis

class BarangAdmin(admin.ModelAdmin):
    list_display = ['kdbrg', 'namabrg', 'stok', 'harga', 'jenis_id', 'waktu_posting', 'link_gbr']
    search_fields = ('kdbrg', 'namabrg', 'jenis_id__nama') # __nama digunakan untuk memilih kolom mana yang akan dipakai untuk relasi dan ditampilkan
    list_filter = ('jenis_id',)
    list_per_page = 3
    ordering = ('stok',)

admin.site.register(Barang, BarangAdmin)
admin.site.register(Jenis)