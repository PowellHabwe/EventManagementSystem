# Generated by Django 4.0.6 on 2022-08-16 15:52

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0044_alter_post_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='id',
        ),
        migrations.AlterField(
            model_name='post',
            name='uuid',
            field=models.CharField(default=uuid.uuid4, max_length=50, primary_key=True, serialize=False),
        ),
    ]
