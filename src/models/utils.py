import math
import random
from models.models import EnglishWord, KoreanWord, Profile, Accuracy, History

def is_success_streaking(history):
    streak = 0
    for h in range(len(history)):
        if (history[h].success):
            streak = streak + 1
        else:
            streak = 0
    return (streak >= 5)

def is_fail_streaking(history):
    streak = 0
    for h in range(len(history)):
        if (history[h].success):
            streak = 0
        else:
            streak = streak + 1
    return (streak >= 5)

def get_max_level(xp):
    if (xp < 800):
        return 1
    if (xp < 2000):
        return 2
    if (xp < 3000):
        return 3
    if (xp < 4200):
        return 4
    if (xp < 5500):
        return 5
    if (xp < 7500):
        return 6
    if (xp < 10000):
        return 7
    if (xp < 14000):
        return 8
    if (xp < 20000):
        return 9
    return 10

def pick_next_word(profile):
    items = list(EnglishWord.objects.filter(korean__level__lt=(get_max_level(profile.xp) + 1)))
    history =  History.objects.filter(Profil=profile).order_by('datetime')
    acc = Accuracy.objects.filter(profile=profile)

    # Remove words from recent history
    for i in range(len(history)):
      if (history[i].word in items):
        items.remove(history[i].word)

    # Give new word if not many words have been guessed
    if (len(acc) <= 50):
      acc = Accuracy.objects.filter(profile=profile)
      for i in range(len(acc)):
        if acc[i].word in items:
          items.remove(acc[i].word)
      return random.choice(items)

    # If user is on a fail streak, give him an easyer word
    if (is_success_streaking(history)):
        ord_acc = acc.order_by('score')
        high_acc = ord_acc[math.ceil(len(ord_acc) / 2):]
        for i in range(len(high_acc)):
            if (high_acc[i].word in items):
                items.remove(high_acc[i].word)
        return random.choice(items)

    # If user is on a success streak, give him a harder word
    if (is_fail_streaking(history)):
        ord_acc = acc.order_by('score')
        low_acc = ord_acc[:math.ceil(len(ord_acc) / 2)]
        for i in range(len(low_acc)):
            if (low_acc[i].word in items):
                items.remove(low_acc[i].word)
        return random.choice(items)
    
    return random.choice(items)
