# Generated by Django 4.0.6 on 2022-08-26 09:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0047_mpesacallstkbacks2_mpesastkcalls_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MpesaStkCalls',
            new_name='MpesaPaymentCalls',
        ),
        migrations.AlterModelOptions(
            name='mpesapaymentcalls',
            options={},
        ),
    ]