# Generated by Django 4.0.6 on 2022-08-26 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0049_delete_log_delete_mpesacallstkbacks2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='mpesapaymentcalls',
            name='MerchantRequestID',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]