from django.shortcuts import render
from TiendaApp.models import producto,trabajadores,clientes
from TiendaApp.forms import ProductoForm,ClienteForm,TrbajadorForm

# Create your views here.


def mostrar_producto(request):
    context={
        "form":ProductoForm(),
    }
    return render(request,"TiendaApp/productos.html",context)

def agregar_producto(request):
    prod_form = ProductoForm(request.POST)
    prod_form.save()
    context = {
        "form":ProductoForm()
    }
    return render(request,"TiendaApp/productos.html",context)

    

def index(request):
    return render(request,"TiendaApp/index.html")

def mostrar_clientes(request):
    context={
        "form":ClienteForm(),
    }
    return render(request,"TiendaApp/clientes.html",context)

def agregar_cliente(request):
    cli_form = ClienteForm(request.POST)
    cli_form.save()
    context = {
        "form":ClienteForm()
    }
    return render(request,"TiendaApp/clientes.html",context)



def mostrar_trabajadores(request):
    context={
        "form":TrbajadorForm(),
    }
    return render(request,"TiendaApp/trabajdores.html",context)

def agregar_trabajadores(request):
    trab_form = TrbajadorForm(request.POST)
    trab_form.save()
    context = {
        "form":ClienteForm()
    }
    return render(request,"TiendaApp/trabajdores.html",context)
