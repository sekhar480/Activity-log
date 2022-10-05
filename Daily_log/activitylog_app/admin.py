from django.contrib import admin
from .models import Satellite,Comment

admin.site.register(Satellite)
# admin.site.register(Comment)

# Register your models here.
@admin.register(Comment)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'date_time', 'satellite', 'subsystem_type', 'details','photo','upload')
    list_filter = ('satellite', 'date_time', 'subsystem_type')
    search_fields = ('satellite','detail', 'date_time')
