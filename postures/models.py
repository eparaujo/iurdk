from django.db import models
from karatestyles.models import KarateStyle

# Create your models here.
class Posture(models.Model):
    style       = models.ForeignKey(KarateStyle, on_delete=models.DO_NOTHING, related_name='posture_style')
    description = models.CharField(max_length=200, blank=True, null=True)
    file        = models.FileField(upload_to='movimentos/', blank=True, null=True)

    def __str__(self):
        return self.description