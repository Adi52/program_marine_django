# Generated by Django 3.0.4 on 2020-04-02 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marine', '0004_auto_20200328_0045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parkingplace',
            name='occupied_to',
            field=models.DateField(blank=True, null=True, verbose_name='Occupied to'),
        ),
    ]
