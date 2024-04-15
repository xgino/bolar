from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('create_date', 'name', 'company', 'email', 'service', 'website')
    list_filter = ('service', )
    search_fields = ('name', 'company', 'email', 'website')

admin.site.register(Contact, ContactAdmin)