from django.contrib import admin
from classes.models import Aula


# Register your models here.
@admin.register(Aula)
class AulaAdmin(admin.ModelAdmin):
    list_display=('id', 'description', 'day', 'turno')