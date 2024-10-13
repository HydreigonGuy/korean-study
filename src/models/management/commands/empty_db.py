from django.core.management.base import BaseCommand, CommandError
from models.models import KoreanWord, EnglishWord, History, Accuracy


class Command(BaseCommand):
    help = "Empties DB"

    def handle(self, *args, **options):
        History.objects.all().delete()
        Accuracy.objects.all().delete()
        KoreanWord.objects.all().delete()
        EnglishWord.objects.all().delete()
