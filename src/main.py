
from file_loader import retrieve_file_contents, FILES_PATH
from random_word_picker import random_word_picker

contents = retrieve_file_contents(FILES_PATH)

for _ in range(20):
    print(random_word_picker(contents))
