from django.db import models
from Service.models import Service
from django.core.validators import URLValidator

class Quote(models.Model):
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    kvk = models.CharField(max_length=20, blank=True, null=True)
    website = models.URLField(validators=[URLValidator()])
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    
    create_date = models.DateTimeField(auto_now_add=True)
    remarks = models.TextField(blank=True)

    # Fields to store service details
    service_category = models.CharField(max_length=100, blank=True)
    service_internal_note = models.CharField(max_length=100, blank=True)
    service_name = models.CharField(max_length=100, blank=True)
    service_quantity = models.IntegerField(blank=True, null=True)
    service_total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    service_discount_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    service_total_after_discount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def save(self, *args, **kwargs):
        # Populate the service details fields from the selected service
        if self.service:
            self.service_category = self.service.service_category.name
            self.service_internal_note = self.service.service_category.internal_note
            self.service_name = self.service.name
            self.service_quantity = self.service.quantity
            self.service_total_price = self.service.total_price
            self.service_discount_amount = self.service.discount_amount
            self.service_total_after_discount = self.service.total_after_discount
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} {self.company}"
    


class DownloadRecord(models.Model):
    email = models.EmailField()
    datetime = models.DateTimeField(auto_now_add=True)
    file_name = models.CharField(max_length=100)
    file_path = models.CharField(max_length=255)  # New field

    def __str__(self):
        return f'{self.email} - {self.file_name} - {self.datetime}'