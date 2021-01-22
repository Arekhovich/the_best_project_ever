# Generated by Django 3.1.3 on 2020-12-10 09:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0017_ratebookuser_rate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)])),
            ],
        ),
        migrations.RemoveField(
            model_name='book',
            name='book_rate',
        ),
        migrations.DeleteModel(
            name='RateBookUser',
        ),
    ]
