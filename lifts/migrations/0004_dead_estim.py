# Generated by Django 5.0.1 on 2024-01-13 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lifts', '0003_dead_squat'),
    ]

    operations = [
        migrations.AddField(
            model_name='dead',
            name='estim',
            field=models.FloatField(null=True),
        ),
    ]