from django.contrib import admin
from dojos.models import Dojo
# Register your models here.

@admin.register(Dojo)
class DojoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'sensei', 'site', 'phone', 'email', 'street', 'number', 'zipcode', 'district', 'city', 'state')