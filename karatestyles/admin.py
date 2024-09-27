from django.contrib import admin
from karatestyles.models import KarateStyle

# Register your models here.
@admin.register(KarateStyle)
class KarateStyleAdmin(admin.ModelAdmin):
    list_display = ('id', 'style', 'origin_style', 'bases', 'qtde_katas')