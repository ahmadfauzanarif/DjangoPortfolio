from django.shortcuts import render
from . models import About
from . forms import FormBarang ## penggunaan titik karena dalam 1 folder

def home(request):
    about = About.objects.first()  ## KODE ORM DJANGO
    return render(request, 'index.html', {'about':about})
def cerita(request):
    return render(request, 'cerita.html')
def berita(request):
    return render(request, 'berita.html')
def tambah_brg(request):
    form_brg = FormBarang()
    return render(request, 'tambah_brg.html', {'form_brg':form_brg})