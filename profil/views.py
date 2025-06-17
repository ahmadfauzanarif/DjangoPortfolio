from django.shortcuts import render
from . models import About
# Create your views here.

def home(request):
    about = About.objects.first()  ## KODE ORM DJANGO
    return render(request, 'index.html', {'about':about})
def cerita(request):
    return render(request, 'cerita.html')
def berita(request):
    return render(request, 'berita.html')