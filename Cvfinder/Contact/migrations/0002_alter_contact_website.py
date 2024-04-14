# Generated by Django 3.2.25 on 2024-04-13 17:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='website',
            field=models.URLField(validators=[django.core.validators.validate_ipv46_address]),
        ),
    ]
