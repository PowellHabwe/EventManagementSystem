# Generated by Django 4.0.6 on 2022-09-28 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0080_rename_event_price_mpesapaymentcalls_event_price_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExistingReceipts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receipt', models.TextField()),
            ],
        ),
    ]
