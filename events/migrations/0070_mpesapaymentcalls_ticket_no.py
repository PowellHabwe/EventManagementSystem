# Generated by Django 4.0.6 on 2022-09-21 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0069_mpesapaymentcalls_mpesa_receipt'),
    ]

    operations = [
        migrations.AddField(
            model_name='mpesapaymentcalls',
            name='ticket_no',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
