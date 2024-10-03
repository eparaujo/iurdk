from django.contrib import admin
from weekdays.models import WeekDay

# Register your models here.
@admin.register(WeekDay)
class WeekDayAdmin(admin.ModelAdmin):
    list_display=('id', 'dayname')