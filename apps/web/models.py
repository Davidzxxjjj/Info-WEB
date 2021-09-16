from django.db import models

# Create your models here.

class veterinaria(models.Model):
    pk_Veterinaria = models.AutoField(primary_key=True, null=False, blank=False)
    ubicacion = models.TextField(null=False, blank=False)
    correo = models.TextField(null=False, blank=False)
    facebook = models.TextField(null=False, blank=False)
    telefono = models.IntegerField(null=False, blank=False)

class producto(models.Model):
    pk_producto = models.AutoField(primary_key=True, null=False, blank=False)
    nombre = models.TextField(null=False, blank=False)
    descripcion = models.TextField(null=False, blank=False)
    cantidad = models.IntegerField(null=False, blank=False)
    precio = models.IntegerField(null=False, blank=False)

class mascota(models.Model):
    pk_mascota = models.AutoField(primary_key=True, null=False, blank=False)
    nombre_mascota = models.TextField(null=False, blank=False)
    raza = models.TextField(null=False, blank=False)
    color = models.TextField(null=False, blank=False)
    edad = models.IntegerField(null=False, blank=False)
