from django.db import models
from dojos.models import Dojo


WEEK = (
    ('SEG', 'Segunda-feira'),
    ('TER', 'Terça-feira'),
    ('QUA', 'Quarta-feira'),
    ('QUI', 'Quinta-feira'),
    ('SEX', 'Sexta-feira'),
    ('SAB', 'Sábado'),
    ('DOM', 'Domingo'),
)

TIMES = (
    ('1º', '10:00 - 11:15'),
    ('2º', '18:00 - 19:15'),
    ('3º', '19:30 - 20:45'),
    ('4º', '10:00 - 12:00')
)

# Create your models here.
class Time(models.Model):
    day = models.CharField(max_length=60, choices=WEEK)
    time = models.CharField(max_length=40, choices=TIMES)
    dojo = models.ForeignKey(Dojo, on_delete=models.DO_NOTHING, related_name='dojo_time', null=True)

    def __str__(self):
        return self.day