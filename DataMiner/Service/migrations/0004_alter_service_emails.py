# Generated by Django 3.2.25 on 2024-04-14 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Service', '0003_alter_service_emails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='emails',
            field=models.IntegerField(blank=True, max_length=100, null=True),
        ),
    ]