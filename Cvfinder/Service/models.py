from django.db import models

class Service(models.Model):

    name = models.CharField(max_length=100, null=True, blank=True)
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    emails = models.IntegerField(null=True, blank=True)
    #add active else Turn Off

    def __str__(self):
        return self.name