from django.db import models

class Equipo(models.Model):
    Nombre = models.CharField(max_length=150)
    Integrante1 = models.CharField(max_length=150)
    Integrante2 = models.CharField(max_length=150)
    Integrante3 = models.CharField(max_length=150)
    Integrante4 = models.CharField(max_length=150)
    Integrante5 = models.CharField(max_length=150)
    email= models.EmailField(max_length=150)

    def __unicode__(self):
        return self.Nombre
