# Generated by Django 4.0.6 on 2022-07-30 21:07

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0024_alter_ticket_info_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket_info',
            name='uuid',
            field=models.CharField(default=uuid.uuid4, max_length=50),
        ),
        migrations.AlterField(
            model_name='ticket_info',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]