# Generated by Django 3.0.7 on 2020-07-06 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='profile',
            name='field_of_interest',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
