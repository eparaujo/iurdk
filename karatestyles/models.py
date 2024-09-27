from django.db import models


# Create your models here.cls
class KarateStyle(models.Model):
    style           = models.CharField(max_length=100)
    origin_style    = models.CharField(max_length=100, blank=True, null=True)
    bases           = models.CharField(max_length=100, blank=True, null=True)
    qtde_katas      = models.CharField(max_length=100, blank=True,null=True)

    def __str__(self):
        return self.style