from django.db import models

# Create your models here.

class Jenis(models.Model):
    nama = models.CharField(max_length=20)
    deskripsi = models.TextField()

    def __str__(self):
        return self.nama

class Barang(models.Model):
    kdbrg = models.CharField(max_length=8)
    namabrg = models.CharField(max_length=75)
    stok = models.IntegerField()
    harga = models.BigIntegerField()
    link_gbr = models.CharField(max_length=150, blank=True)
    jenis_id = models.ForeignKey(Jenis, on_delete=models.CASCADE, null=True)
    waktu_posting = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.namabrg

class About(models.Model):
    judul = models.CharField(max_length=200)
    isi = models.TextField()
    image = models.ImageField(upload_to='')
    
    def __str__(self):
        return self.judul
