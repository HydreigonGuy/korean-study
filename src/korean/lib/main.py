
from file_loader import retrieve_file_contents, FILES_PATH
from random_word_picker import random_word_picker

contents = retrieve_file_contents(FILES_PATH)

print(len(contents))

for _ in range(20):
    word = random_word_picker(contents)
    print(word["eng"] + ": " + word["kor"])
