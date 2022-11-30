# Generated by Django 4.0.6 on 2022-08-26 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0050_mpesapaymentcalls_merchantrequestid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mpesapaymentcalls',
            old_name='ResponseDescription',
            new_name='ItemAmount',
        ),
        migrations.RenameField(
            model_name='mpesapaymentcalls',
            old_name='ResultCode',
            new_name='ItemDate',
        ),
        migrations.RenameField(
            model_name='mpesapaymentcalls',
            old_name='ResultDesc',
            new_name='ItemNumber',
        ),
        migrations.RenameField(
            model_name='mpesapaymentcalls',
            old_name='ResponseCode',
            new_name='TransactionStatus1',
        ),
        migrations.AddField(
            model_name='mpesapaymentcalls',
            name='ItemReceipt',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mpesapaymentcalls',
            name='TransactionDescription1',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mpesapaymentcalls',
            name='TransactionDescription2',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mpesapaymentcalls',
            name='TransactionStatus2',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]