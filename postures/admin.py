from django.contrib import admin
from postures.models import Posture

# Register your models here.
@admin.register(Posture)
class PostureAdmin(admin.ModelAdmin):
    list_display = ('id', 'style', 'description', 'file')