from django.db import models

# Create your models here.

class producto(models.Model):
   id= models.AutoField(primary_key=True)
   producto = models.CharField(max_length=20)
   stok= models.IntegerField()


class trabajadores(models.Model):
    id= models.AutoField(primary_key=True)
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    sueldo= models.IntegerField()
    cargo = models.CharField(max_length=30)

class clientes(models.Model):
    id= models.AutoField(primary_key=True)
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    recurrencia = models.IntegerField()