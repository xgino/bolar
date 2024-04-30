from django.db import models
from django.core.exceptions import ValidationError
import os
from PIL import Image
from django.core.files.base import ContentFile
from io import BytesIO


def resize_image(image_field, width, height):
    img = Image.open(image_field)
    img.thumbnail((width, height), Image.ANTIALIAS)
    
    # Prepare the image to be saved
    output_io_stream = BytesIO()
    img.save(output_io_stream, format='PNG', quality=100)
    output_io_stream.seek(0)
    
    # Save the resized image back to the image field
    image_field.save(image_field.name, ContentFile(output_io_stream.read()), save=False)


class Site(models.Model):
    name = models.CharField(max_length=255)
    about = models.TextField(max_length=255, null=True, blank=True)
    street = models.CharField(max_length=255, null=True, blank=True)
    zip = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    kvk = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    mail = models.CharField(max_length=255, null=True, blank=True)
    favicon = models.ImageField(upload_to='site', default='site/favicon.png', null=True, blank=True)
    logo = models.ImageField(upload_to='site', default='site/logo.png', null=True, blank=True)

    def __str__(self):
        return self.name

    def clean(self):
        existing_count = Site.objects.count()

        if not self.id and existing_count >= 1:
            raise ValidationError('Only one instance of Site is allowed.')

    def save(self, *args, **kwargs):
        self.clean()  # Validate before saving

         # Resize favicon
        if self.favicon:
            resize_image(self.favicon, 25, 25)

        # Resize logo
        if self.logo:
            resize_image(self.logo, 200, 200)

        super().save(*args, **kwargs)