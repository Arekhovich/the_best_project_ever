# Generated by Django 3.1.3 on 2020-12-19 07:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('manager', '0027_auto_20201218_1744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='tmp_book',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='manager.tmpbook'),
        ),
        migrations.AlterField(
            model_name='likebookuser',
            name='tmp_book',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='liked_user_table', to='manager.tmpbook'),
        ),
    ]
