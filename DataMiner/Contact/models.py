from django.db import models
from Service.models import Service
from django.core.validators import URLValidator

class Contact(models.Model):
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    kvk = models.CharField(max_length=20, blank=True, null=True)
    website = models.URLField(validators=[URLValidator()])
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)

    remarks = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} {self.company}"