# Generated by Django 4.1.3 on 2022-11-26 14:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('category', models.TextField(blank=True)),
            ],
        ),
    ]
