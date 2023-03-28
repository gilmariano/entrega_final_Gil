from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Pesca(models.Model):
    nombre = models.CharField(max_length=50)
    detalle = models.TextField(max_length=1000)
    peso = models.FloatField()
    imagen = models.ImageField(upload_to="lista", null=True, blank=True)
    propietario = models.ForeignKey(to=User, on_delete=models.CASCADE , related_name = "propietario")

    @property
    def image_url(self):
        return self.imagen.url if self.imagen else ''
    
    def __str__(self):
        return f' {self.id} - {self.nombre} - {self.propietario.id} '

class Profile(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name="profile")
    avatar = models.ImageField(upload_to="avatares", null=True, blank=True)