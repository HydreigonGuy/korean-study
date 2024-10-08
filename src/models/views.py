
from django.http import HttpResponse
from django.template import loader
import json
import random
from models.models import EnglishWord, KoreanWord

def index(request):
  if request.user.is_authenticated:
    template = loader.get_template('index.html')
    return HttpResponse(template.render())
  else:
    template = loader.get_template('visitor.html')
    return HttpResponse(template.render())

def get_word(request):
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
