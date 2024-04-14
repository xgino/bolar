from django.contrib import admin
from .models import Service

 
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'discounted_price', 'price', 'emails', 'active')
    list_filter = ('active',)