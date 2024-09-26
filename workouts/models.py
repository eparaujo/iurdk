from django.db import models
from karatestyles.models import KarateStyle


# Create your models here.
class Workout(models.Model):
    style =  models.ForeignKey(KarateStyle, on_delete=models.DO_NOTHING, related_name='workout_style')
    description = models.TextField(blank=True, null=True)
    movie_workout = models.FileField(upload_to='workout/', blank=True, null=True)