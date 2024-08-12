from django.core.management.base import BaseCommand, CommandError
from models.models import KoreanWord, EnglishWord

import os
import json

class Command(BaseCommand):
    help = "Loads Vocab into DB"


    FILES_PATH = "../vocab"


    def retrieve_file_contents(self, path):
        contents = {}

        if os.path.isdir(path):
            files = os.listdir(path)
            for f in files:
                data = self.retrieve_file_contents(os.path.join(path, f))
                for d in data:
                    contents[d] = data[d]
        elif os.path.isfile(path):
            file = open(path)
            data = json.loads(file.read())
            file.close()
            for d in data:
                contents[d] = data[d]
        return (contents)

    def add_arguments(self, parser):
        parser.add_argument("path", type=str)

    def handle(self, *args, **options):
        print(self.retrieve_file_contents(options["path"]))
