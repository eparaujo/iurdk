from django.contrib import admin
from dojos.models import Dojo



# Register your models here.
@admin.register(Dojo)
class DojoAdmin(admin.ModelAdmin):
    list_display= (
        'razaosocial',
        'tradename',
        'site',
        'email',
        'whatsapp',
        'phone',
        'street',
        'number',
        'zipcode',
        'district',
        'city',
        'state',
        'country',     
        )