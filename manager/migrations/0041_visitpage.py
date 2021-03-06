# Generated by Django 3.1.3 on 2021-01-08 11:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('manager', '0040_auto_20210107_2237'),
    ]

    operations = [
        migrations.CreateModel(
            name='VisitPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='visit_book', to='manager.book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='visit_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'book')},
            },
        ),
    ]
