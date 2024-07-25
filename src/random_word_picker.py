
import random
import time

random.seed(time.time())

def random_word_picker(word_list):
    key = list(word_list.keys())[random.randint(0, len(word_list))]
    return {key:word_list[key]}
