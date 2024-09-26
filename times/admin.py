from django.contrib import admin
from times.models import Time

# Register your models here.
@admin.register(Time)
class TimeAdmin(admin.ModelAdmin):
    list_display = ('id', 'day', 'time', 'dojo')