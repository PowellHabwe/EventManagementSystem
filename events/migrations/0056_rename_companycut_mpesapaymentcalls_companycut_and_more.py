# Generated by Django 4.0.6 on 2022-09-07 13:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0055_mpesapaymentcalls_companycut'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mpesapaymentcalls',
            old_name='companycut',
            new_name='Companycut',
        ),
        migrations.RenameField(
            model_name='mpesapaymentcalls',
            old_name='organiserscut',
            new_name='Organiserscut',
        ),
    ]
