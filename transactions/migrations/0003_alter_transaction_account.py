# Generated by Django 4.1.3 on 2023-01-09 09:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0002_transaction_type_account_transaction_account'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transactions.account'),
        ),
    ]
