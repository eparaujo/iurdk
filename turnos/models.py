from django.db import models

# Create your models here.
class Turno(models.Model):

    idTurno = models.IntegerField()
    name    = models.CharField(max_length=100)
    start   = models.TimeField()
    end     = models.TimeField()

    def __str__(self):
        return self.name