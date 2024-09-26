from django.db import models


# Create your models here.cls
class KarateStyle(models.Model):
    style           = models.CharField(max_length=100)
    #gran_master     = models.CharField(max_length=100, blank=True, null=True)
    #province_origin = models.CharField(max_length=160, blank=True, null=True)
    #year_create     = models.IntegerField()

    def __str__(self):
        return self.style