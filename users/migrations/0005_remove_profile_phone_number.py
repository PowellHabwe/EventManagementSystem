# Generated by Django 4.0.6 on 2022-09-21 21:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_profile_phone_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='phone_number',
        ),
    ]