# Generated by Django 4.0.6 on 2022-10-31 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0082_rename_existingreceipts_existingreceipt'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventTotals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Event_title', models.TextField()),
                ('withdrawal_id', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='b2c',
            name='withdrawal_id',
            field=models.CharField(default=1, max_length=10000000),
            preserve_default=False,
        ),
    ]
