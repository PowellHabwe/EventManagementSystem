# Generated by Django 4.0.6 on 2022-07-29 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0020_alter_ticket_info_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ticket_info',
            old_name='price',
            new_name='ticket_price',
        ),
    ]
