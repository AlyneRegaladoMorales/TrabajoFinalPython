"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from TiendaApp.views import index
from TiendaApp.views import mostrar_clientes
from TiendaApp.views import mostrar_producto
from TiendaApp.views import mostrar_trabajadores



urlpatterns = [

    path('', index, name="index"),    
    path('admin/', admin.site.urls),
    path('clientes/',mostrar_clientes,name="clientes"),
    path('productos/',mostrar_producto,name="productos"),
    path('trabajdores/',mostrar_trabajadores,name="trabajdores"),
    

]