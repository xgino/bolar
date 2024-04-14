# Generated by Django 3.2.25 on 2024-04-14 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Service', '0004_alter_service_emails'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='emails',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
