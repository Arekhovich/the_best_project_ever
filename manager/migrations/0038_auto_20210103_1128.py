# Generated by Django 3.1.3 on 2021-01-03 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0037_book_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='text',
            field=models.TextField(max_length=1200, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(max_length=120),
        ),
    ]
