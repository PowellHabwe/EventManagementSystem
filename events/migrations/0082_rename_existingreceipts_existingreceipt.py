# Generated by Django 4.0.6 on 2022-09-28 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0081_existingreceipts'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ExistingReceipts',
            new_name='ExistingReceipt',
        ),
    ]
