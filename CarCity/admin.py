from django.contrib import admin
from .models import Ad

class AdAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'year', 'price', 'user')
    list_filter = ('brand', 'model', 'year')
    search_fields = ('brand', 'model', 'year')
    ordering = ('-year', 'brand', 'model')

admin.site.register(Ad, AdAdmin)
