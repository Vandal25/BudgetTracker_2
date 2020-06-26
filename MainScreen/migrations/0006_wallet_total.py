# Generated by Django 3.0.5 on 2020-05-23 21:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MainScreen', '0005_wallet'),
    ]

    operations = [
        migrations.AddField(
            model_name='wallet',
            name='total',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='MainScreen.Transaction'),
            preserve_default=False,
        ),
    ]