from django.shortcuts import render
from .models import Projecto

# Create your views here.
def portafolio(request):
    projectos = Projecto.objects.all()
    return render(request,"portafolio/portafolio.html", {'projectos':projectos})