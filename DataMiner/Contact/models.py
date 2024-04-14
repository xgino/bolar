from django.db import models
from Service.models import Service
from django.core.validators import RegexValidator

class LessStrictURLField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_length', 200)  # Set the maximum length of the URL
        super().__init__(*args, **kwargs)


class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    kvk = models.CharField(max_length=20, blank=True, null=True)
    website = LessStrictURLField()
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)

    remarks = models.TextField(blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"