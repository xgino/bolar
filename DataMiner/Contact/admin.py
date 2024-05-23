from django.contrib import admin
from .models import Quote, DownloadRecord

@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'email', 'phone', 'service_category', 'service_internal_note', 'service_name', 'service_quantity', 'service_total_price', 'service_discount_amount', 'service_total_after_discount', 'create_date')
    readonly_fields = ('service_category', 'service_internal_note', 'service_name', 'service_quantity', 'service_total_price', 'service_discount_amount', 'service_total_after_discount')

    def get_readonly_fields(self, request, obj=None):
        # Make service fields read-only when editing existing quote
        if obj:
            return self.readonly_fields + ('service',)
        return self.readonly_fields

@admin.register(DownloadRecord)
class DownloadRecordAdmin(admin.ModelAdmin):
    list_display = ('email', 'datetime', 'file_name', 'file_path')
    search_fields = ('email', 'file_name')
    list_filter = ('datetime',)