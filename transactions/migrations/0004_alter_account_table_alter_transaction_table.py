# Generated by Django 4.1.3 on 2023-02-13 07:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0003_alter_transaction_account'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='account',
            table='accounts',
        ),
        migrations.AlterModelTable(
            name='transaction',
            table='transactions',
        ),
    ]
