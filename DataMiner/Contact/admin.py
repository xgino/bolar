from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('create_date', 'first_name', 'last_name', 'email', 'service', 'website')
    list_filter = ('service', )
    search_fields = ('first_name', 'last_name', 'email', 'website')

admin.site.register(Contact, ContactAdmin)