# Generated by Django 4.0.5 on 2022-06-29 19:04

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0010_alter_post_uuid_f'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='uuid_f',
        ),
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
    ]
