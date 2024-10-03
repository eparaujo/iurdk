from django.db import models
from classes.models import Aula


# Create your models here.
class Dojo(models.Model):
    razaosocial = models.CharField(max_length=200)
    tradename   = models.CharField(max_length=200, blank=True, null=True)
    site        = models.CharField(max_length=200, blank=True, null=True)
    email       = models.EmailField(max_length=200, unique=True)
    whatsapp    = models.CharField(max_length=60, blank=True, null=True)
    phone       = models.CharField(max_length=60, blank=True, null=True)
    street      = models.CharField(max_length=200, blank=True, null=True)
    number      = models.IntegerField()
    zipcode     = models.CharField(max_length=20, blank=True, null=True)
    district    = models.CharField(max_length=160, blank=True, null=True)
    city        = models.CharField(max_length=160, blank=True, null=True)
    state       = models.CharField(max_length=160, blank=True, null=True)
    country     = models.CharField(max_length=160, blank=True, null=True)
    aulas       = models.ForeignKey(Aula, on_delete=models.DO_NOTHING, related_name='auladojo', blank=True, null=True)

    def __str__(self):
        return self.tradename
