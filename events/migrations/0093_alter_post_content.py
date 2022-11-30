# Generated by Django 4.0.6 on 2022-11-22 07:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0092_rename_number_receiving_mpesapaymentcalls_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(validators=[django.core.validators.MinLengthValidator(50)]),
        ),
    ]
