# Generated by Django 4.0.6 on 2022-09-09 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0062_remove_post_id_alter_post_uuid'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyCut',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='OrganiserCut',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
            ],
        ),
    ]