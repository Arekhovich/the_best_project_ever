# Generated by Django 3.1.3 on 2021-01-08 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0041_visitpage'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='git_token',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
    ]
