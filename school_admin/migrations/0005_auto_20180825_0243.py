# Generated by Django 2.1 on 2018-08-24 17:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('school_admin', '0004_invoice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attend',
            name='attended',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='受講日'),
        ),
    ]
