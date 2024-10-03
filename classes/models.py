from django.db import models
from weekdays.models import WeekDay
from turnos.models import Turno


# Create your models here.
class Aula(models.Model):
    description = models.CharField(max_length=160)
    day = models.ForeignKey(WeekDay, on_delete=models.DO_NOTHING, blank=True, null=True)
    turno = models.ForeignKey(Turno, on_delete=models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return self.description