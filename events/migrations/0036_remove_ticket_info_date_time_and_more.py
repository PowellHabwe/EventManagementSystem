# Generated by Django 4.0.6 on 2022-08-16 11:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0035_rename_date_ticket_info_event_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket_info',
            name='date_time',
        ),
        migrations.RemoveField(
            model_name='ticket_info',
            name='event_date',
        ),
        migrations.RemoveField(
            model_name='ticket_info',
            name='time',
        ),
    ]