from django.db import models
from dojos.models import Dojo
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class ReviewDojo(models.Model):
    dojo = models.ForeignKey(Dojo, on_delete=models.DO_NOTHING, related_name='dojos')
    stars   = models.IntegerField(
        validators=[
            MinValueValidator(0, 'Não é permitida avaliação inferior a ZERO!'),
            MaxValueValidator(5, 'Não é permitida avaliação superior a CINCO!'),
        ]
    )
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.dojo