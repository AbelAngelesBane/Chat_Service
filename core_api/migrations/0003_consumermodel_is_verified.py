# Generated by Django 3.2.9 on 2024-04-16 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_api', '0002_consumermodel_register_as'),
    ]

    operations = [
        migrations.AddField(
            model_name='consumermodel',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
    ]
