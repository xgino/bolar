# Generated by Django 3.2.25 on 2024-05-20 15:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Service', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='scraper_name',
            new_name='name',
        ),
    ]
