from django.contrib import admin
from graduations.models import Graduation


# Register your models here.
@admin.register(Graduation)
class GraduationAdmin(admin.ModelAdmin):
    list_display=('id', 'name')