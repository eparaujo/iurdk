from django.db import models
from karatestyles.models import KarateStyle


# Create your models here.
class Kata(models.Model):
    style          = models.ForeignKey(KarateStyle, on_delete=models.DO_NOTHING, related_name='styles')
    namekata       = models.CharField(max_length=100)
    qtde_moviments = models.IntegerField()
    data_upload    = models.DateTimeField(auto_now_add=True)
    file           = models.FileField(upload_to='videos/', blank=True, null=True)
    link           = models.URLField(max_length=300, blank=True, null=True)
    duracao        = models.IntegerField(null=True, blank=True) # Duração do vídeo (opcional, em segundos)

    def __str__(self):
        return self.namekata