# Generated by Django 3.1.3 on 2020-12-18 14:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('manager', '0026_auto_20201212_1244'),
    ]

    operations = [
        migrations.CreateModel(
            name='TMPBook',
            fields=[
                ('title', models.CharField(help_text='ну это типа имя книги', max_length=50, verbose_name='Название')),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('text', models.TextField(max_length=200, null=True)),
                ('rate', models.DecimalField(decimal_places=2, default=0.0, max_digits=3)),
                ('count_rated_users', models.PositiveIntegerField(default=0)),
                ('count_all_stars', models.PositiveIntegerField(default=0)),
                ('slug', models.SlugField(primary_key=True, serialize=False)),
                ('authors', models.ManyToManyField(related_name='tmp_books', to=settings.AUTH_USER_MODEL)),
                ('users_like', models.ManyToManyField(related_name='tmp_liked_books', through='manager.LikeBookUser', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='tmp_book',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tmp_comments', to='manager.tmpbook'),
        ),
        migrations.AddField(
            model_name='likebookuser',
            name='tmp_book',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tmp_rates', to='manager.tmpbook'),
        ),
    ]