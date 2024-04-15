# Generated by Django 3.2.9 on 2024-04-15 21:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ConsumerModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=8)),
                ('name', models.CharField(max_length=40)),
                ('birthdate', models.DateField(blank=True, null=True)),
                ('mobile_number', models.CharField(blank=True, max_length=12, null=True)),
                ('gender', models.CharField(blank=True, choices=[('male', 'MALE'), ('female', 'FEMALE'), ('lgbt', 'LGBT')], max_length=20, null=True)),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
