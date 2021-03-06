# Generated by Django 3.0.5 on 2020-06-18 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainScreen', '0007_auto_20200618_2050'),
    ]

    operations = [
        migrations.AddField(
            model_name='wallet',
            name='total',
            field=models.FloatField(default=20),
        ),
        migrations.AlterField(
            model_name='wallet',
            name='expenses',
            field=models.FloatField(default=20),
        ),
        migrations.AlterField(
            model_name='wallet',
            name='revenue',
            field=models.FloatField(default=20),
        ),
    ]
