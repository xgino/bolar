from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.conf import settings

from .models import Site

@receiver(post_migrate)
def create_initial_records(sender, **kwargs):
    # Create initial Site record
    if Site.objects.count() == 0:
        Site.objects.create(
            name='SiteTitle',
            about='Abouttext site server company thngs',
            # Add other fields as needed
        )



