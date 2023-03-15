from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request,"TiendaApp/index.html")

def clientes(request):
    return render(request,"TiendaApp/clientes.html")

def productos(request):
    return render(request,"TiendaApp/productos.html")

def trabajdores(request):
    return render(request,"TiendaApp/trabajdores.html")

