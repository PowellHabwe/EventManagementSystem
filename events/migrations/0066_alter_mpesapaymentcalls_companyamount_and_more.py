# Generated by Django 4.0.6 on 2022-09-09 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0065_alter_mpesapaymentcalls_companyamount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mpesapaymentcalls',
            name='CompanyAmount',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='mpesapaymentcalls',
            name='OrganisersAmount',
            field=models.TextField(),
        ),
    ]