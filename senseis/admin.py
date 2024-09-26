from django.contrib import admin
from senseis.models import Sensei

# Register your models here.
@admin.register(Sensei)
class SenseiAdmin(admin.ModelAdmin):
    list_display = ('name', 'cpf', 'graduation', 'email', 'celPhone')