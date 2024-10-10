from django.db import models
from graduations.models import Graduation
#from dojos.models import Dojo


class Karateca(models.Model):
    register   = models.IntegerField()
    name       = models.CharField(max_length=200)
    cpf        = models.CharField(max_length=30, blank=True, null=True)
    email      = models.EmailField(unique=True)
    celphone   = models.CharField(max_length=60, blank=True, null=True)
    graduation = models.ForeignKey(Graduation, on_delete=models.DO_NOTHING, related_name='graduation', blank=True, null=True)
    #dojo       = models.ManyToManyField(Dojo, related_name='dojokarateca')

    def __str__(self):
        return self.name

