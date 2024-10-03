from django.contrib import admin
from karatecas.models import Karateca


# Register your models here.
@admin.register(Karateca)
class KaratecaAdmin(admin.ModelAdmin):
    list_display= ('id', 'register', 'name', 'cpf', 'email', 'celphone', 'graduation')