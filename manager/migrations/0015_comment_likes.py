# Generated by Django 3.1.3 on 2020-12-10 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0014_book_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='likes',
            field=models.PositiveIntegerField(default=0),
        ),
    ]