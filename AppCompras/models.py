from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Listas(models.Model):
    users = models.ManyToManyField(User)
    nombre = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f'{self.nombre}'


class DetalleLista(models.Model):
    lista = models.ForeignKey(Listas, on_delete=models.CASCADE, related_name='detalles')
    nombre = models.CharField(max_length=250)
    cantidad = models.IntegerField(blank=True,null=True)

    def __str__(self):
        return f'{self.nombre}'