# Generated by Django 5.0.1 on 2024-01-13 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lifts', '0004_dead_estim'),
    ]

    operations = [
        migrations.AddField(
            model_name='bench',
            name='estim',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='squat',
            name='estim',
            field=models.FloatField(null=True),
        ),
    ]