# Generated by Django 4.0.6 on 2022-09-28 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0078_post_id_alter_post_uuid'),
    ]

    operations = [
        migrations.AddField(
            model_name='mpesapaymentcalls',
            name='event_price',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mpesapaymentcalls',
            name='event_title',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mpesapaymentcalls',
            name='withdrawal_code',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
