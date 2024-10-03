from django.contrib import admin
from turnos.models import Turno


# Register your models here.
@admin.register(Turno)
class WeekAdmin(admin.ModelAdmin):
    list_display=('id', 'idTurno', 'name', 'start', 'end')