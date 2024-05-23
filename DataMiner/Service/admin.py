from django.contrib import admin
from .models import Service, ServiceCategory


class ServiceInline(admin.TabularInline):
    model = Service
    extra = 0  # Do not add a new row
    readonly_fields = ('total_price', 'discount_amount', 'total_after_discount', 'cost_per_item_after_discount')
    ordering = ('quantity',)  # Sort by quantity in ascending order

@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'internal_note')
    search_fields = ('name',)
    inlines = [ServiceInline]