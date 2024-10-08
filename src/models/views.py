
from django.http import HttpResponse
from django.template import loader
import json
import random
from models.models import EnglishWord, KoreanWord, Profile, Accuracy

def index(request):
  if request.user.is_authenticated:
    template = loader.get_template('index.html')
    return HttpResponse(template.render())
  else:
    template = loader.get_template('visitor.html')
    return HttpResponse(template.render())

def get_word(request):
  if request.user.is_authenticated:
    prev_word = request.GET.get('word', '')
    prev_res = request.GET.get('res', '')
    if (prev_word != '' or prev_res != ''):
      try:
        previous_word = EnglishWord.objects.get(word=prev_word)
        profile = Profile.objects.get(user=request.user)
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
      except:
        pass
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
  else:
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
