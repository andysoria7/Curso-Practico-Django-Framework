from django.shortcuts import render
from .models import Project

# Create your views here.

def portfolio(request):
    projects = Project.objects.all() # Nos va a devolver todos los objetos que tiene el modelo de proyecto.
    return render(request, 'portfolio/portfolio.html', {'projects': projects})
