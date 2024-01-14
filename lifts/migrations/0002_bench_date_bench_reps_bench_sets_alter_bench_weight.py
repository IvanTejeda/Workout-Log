# Generated by Django 5.0.1 on 2024-01-12 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lifts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bench',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='bench',
            name='reps',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='bench',
            name='sets',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='bench',
            name='weight',
            field=models.IntegerField(null=True),
        ),
    ]