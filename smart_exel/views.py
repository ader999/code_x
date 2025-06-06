from django.shortcuts import render
from .models import PlantillaExcel

def index(request):
    return render(request, 'index.html')

def plantillasexel(request):
    plantillas = PlantillaExcel.objects.all()
    context = {'plantillas': plantillas}
    return render(request, 'plantillasexel.html', context)
