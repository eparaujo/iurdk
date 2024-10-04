from django.contrib import admin
from katas.models import Kata

# Register your models here.

@admin.register(Kata)
class KataAdmin(admin.ModelAdmin):
    list_display = ('style', 'nameKata', 'qtde_moviments', 'data_upload', 'file', 'link','duracao')