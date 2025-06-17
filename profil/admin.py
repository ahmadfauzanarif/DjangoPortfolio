from django.contrib import admin
from .models import Barang, Jenis, About
from unfold.admin import ModelAdmin  # Pakai ModelAdmin dari Unfold

class BarangAdmin(ModelAdmin):  # Ganti ke ModelAdmin dari Unfold
    list_display = ['kdbrg', 'namabrg', 'stok', 'harga', 'jenis_id', 'waktu_posting', 'link_gbr']
    search_fields = ('kdbrg', 'namabrg', 'jenis_id__nama')
    list_filter = ('jenis_id',)
    list_per_page = 3
    ordering = ('stok',)

admin.site.register(Barang, BarangAdmin)
admin.site.register(Jenis)
admin.site.register(About)