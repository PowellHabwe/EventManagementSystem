# Generated by Django 4.0.6 on 2022-09-07 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0053_rename_itemnumber_mpesapaymentcalls_phonenumber2'),
    ]

    operations = [
        migrations.AddField(
            model_name='mpesapaymentcalls',
            name='organiserscut',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
            preserve_default=False,
        ),
    ]
