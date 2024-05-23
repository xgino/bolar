from django.db import models

class ServiceCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name='Service Name')
    description = models.TextField(null=True, blank=True, verbose_name='Description')
    internal_note = models.TextField(null=True, blank=True, verbose_name='Internal Note')

    def __str__(self):
        return self.name

class Service(models.Model):
    service_category = models.ForeignKey(ServiceCategory, related_name='services', on_delete=models.CASCADE, verbose_name='Service Category')
    name = models.CharField(max_length=100, null=True, blank=True, verbose_name='Scraper Name')
    quantity = models.IntegerField(null=True, blank=True, verbose_name='Quantity')
    cost_per_item = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name='Cost per Item (cpi)')
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, verbose_name='Discount Percentage')
    active = models.BooleanField(default=True, verbose_name='Active')

    @property
    def total_price(self):
        if self.quantity is not None and self.cost_per_item is not None:
            return self.quantity * self.cost_per_item
        return None

    @property
    def discount_amount(self):
        if self.total_price is not None and self.discount_percentage is not None:
            return round(self.total_price * self.discount_percentage, 2)
        return None

    @property
    def total_after_discount(self):
        if self.total_price is not None and self.discount_amount is not None:
            return round(self.total_price - self.discount_amount, 2)
        return None
    
    @property
    def cost_per_item_after_discount(self):
        if self.total_after_discount is not None and self.quantity is not None:
            return round(self.total_after_discount / self.quantity, 2)
        return None

    def __str__(self):
        return f"{self.service_category} {self.name}"
    

    def save(self, *args, **kwargs):
        super(Service, self).save(*args, **kwargs)

    def get_range(self):
        if self.quantity is not None:
            # Get all active services ordered by quantity
            services = Service.objects.filter(active=True).order_by('quantity')
            previous_end = 0

            for service in services:
                # Check if the current quantity falls within the range of the current service
                if previous_end < self.quantity <= service.quantity:
                    return f"{previous_end + 1} - {service.quantity}"
                previous_end = service.quantity

            # If the quantity is less than the minimum quantity in the table, set the range to start from 1
            if self.quantity < services.first().quantity:
                return f"1 - {services.first().quantity}"

            # If the quantity exceeds the maximum quantity in the table, set the range to start from the last service's quantity
            if self.quantity > services.last().quantity:
                return f"{previous_end + 1} - {self.quantity}"

        return ""

    # service price table on product page 
    def get_discount_integer(self):
        return int(self.discount_percentage * 100)