# Generated by Django 4.0.6 on 2022-09-26 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0076_b2c'),
    ]

    operations = [
        migrations.AlterField(
            model_name='b2c',
            name='amount',
            field=models.CharField(max_length=10000000),
        ),
        migrations.AlterField(
            model_name='b2c',
            name='phone_no',
            field=models.CharField(max_length=10000000),
        ),
    ]
