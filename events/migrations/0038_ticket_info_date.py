# Generated by Django 4.0.6 on 2022-08-16 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0037_rename_title_promise_ticket_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket_info',
            name='date',
            field=models.DateField(null=True),
        ),
    ]
