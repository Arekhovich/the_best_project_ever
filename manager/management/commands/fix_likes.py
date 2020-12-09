from django.core.management.base import BaseCommand
from django.db.models import Count
from manager.models import Book

class Command(BaseCommand):
    def handle(self, *args, **options):
        book = Book.objects.annotate(count_like=Count("users_like"))
        for b in book:
            b.likes = b.count_like
        Book.objects.bulk_update(book, ('likes'))
