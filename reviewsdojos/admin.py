from django.contrib import admin
from reviewsdojos.models import ReviewDojo

# Register your models here.
@admin.register(ReviewDojo)
class ReviewDojoAdmin(admin.ModelAdmin):
    list_display = ('id', 'dojo', 'stars', 'comment')