# Generated by Django 3.2.25 on 2024-04-14 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Service', '0002_auto_20240413_2046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='emails',
            field=models.CharField(blank=True, choices=[('500', '500 Emails'), ('1500', '1500 Emails'), ('5000', '5000 Emails')], max_length=100, null=True),
        ),
    ]