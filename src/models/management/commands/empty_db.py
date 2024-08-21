from django.core.management.base import BaseCommand, CommandError
from models.models import KoreanWord, EnglishWord


class Command(BaseCommand):
    help = "Empties DB"

    def handle(self, *args, **options):
        KoreanWord.objects.all().delete()
        EnglishWord.objects.all().delete()
