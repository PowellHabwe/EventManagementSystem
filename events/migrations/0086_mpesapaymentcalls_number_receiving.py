# Generated by Django 4.0.6 on 2022-11-01 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0085_alter_eventtotals_event_title_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='mpesapaymentcalls',
            name='number_receiving',
            field=models.CharField(default=1, max_length=10000000),
            preserve_default=False,
        ),
    ]
