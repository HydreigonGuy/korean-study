
from django.http import HttpResponse
from django.template import loader
import json
import random
from models.models import EnglishWord, KoreanWord, Profile, Accuracy, History

def index(request):
  if request.user.is_authenticated:
    template = loader.get_template('index.html')
    return HttpResponse(template.render())
  else:
    template = loader.get_template('visitor.html')
    return HttpResponse(template.render())

def get_word(request):
  if request.user.is_authenticated:
    # For logged in User
    prev_word = request.GET.get('word', '')
    prev_res = request.GET.get('res', '')
    if (prev_word != '' or prev_res != ''):
      # Log previous word
      try:
        previous_word = EnglishWord.objects.get(word=prev_word)
        profile = Profile.objects.get(user=request.user)

        # Log accuracy
        if (Accuracy.objects.filter(word=previous_word, profile=profile).exists()):
          acc = Accuracy.objects.get(word=previous_word, profile=profile)
          acc.total_guesses = acc.total_guesses + 1
          if (prev_res == 'true'):
            acc.correct_guesses = acc.correct_guesses + 1
          acc.save()
        else:
          correct_guesses = 0
          if (prev_res == 'true'):
            correct_guesses = 1
          new_acc = Accuracy(word=previous_word, profile=profile, correct_guesses=correct_guesses, total_guesses=1)
          new_acc.save()
        
        # Log history
        max_history = 5
        new_history = History(word=previous_word, success=False, Profil=profile)
        if (prev_res == 'true'):
          new_history.success = True
        new_history.save()
        while (len(History.objects.filter(Profil=profile)) > max_history):
          History.objects.filter(Profil=profile).order_by('datetime')[0].delete()

      except:
        pass

    # Get next word
    items = list(EnglishWord.objects.all())

    # Remove words from recent history
    history =  History.objects.filter(Profil=profile)
    for i in range(len(history)):
      if (history[i].word in items):
        items.remove(history[i].word)

    # Give new word if not many words have been guessed
    if (len(Accuracy.objects.filter(profile=profile)) <= 50):
      acc = Accuracy.objects.filter(profile=profile)
      for i in range(len(acc)):
        if acc[i].word in items:
          items.remove(acc[i].word)

    random_eng = random.choice(items)
    korean_words = []
    for k in random_eng.korean.all():
      korean_words.append({"word":k.word})
    data = {
      "word":random_eng.word,
      "korean":korean_words
    }
    return HttpResponse(json.dumps(data), content_type='application/json')

  else:
    # For anonymous user
    items = list(EnglishWord.objects.all())
    random_eng = random.choice(items)
    korean_words = []
    for k in random_eng.korean.all():
      korean_words.append({"word":k.word})
    data = {
      "word":random_eng.word,
      "korean":korean_words
    }
    return HttpResponse(json.dumps(data), content_type='application/json')
