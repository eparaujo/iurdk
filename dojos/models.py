from django.db import models
from senseis.models import Sensei


class Dojo(models.Model):
    name     = models.CharField(max_length=200) 
    sensei   = models.ForeignKey(Sensei, on_delete=models.DO_NOTHING ,related_name='senseis')
    site     = models.CharField(max_length=150, blank=True, null=True)
    phone    = models.CharField(max_length=60, blank=True, null=True)
    email    = models.CharField(max_length=160, blank=True, null=True)
    street   = models.CharField(max_length=200, blank=True, null=True)
    number   = models.IntegerField()
    zipcode  = models.CharField(max_length=10, blank=True, null=True)
    district = models.CharField(max_length=100, blank=True, null=True)
    city     = models.CharField(max_length=100, blank=True, null=True)
    state    = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name