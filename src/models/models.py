from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User


class KoreanWord(models.Model):
    word = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    examples = ArrayField(models.CharField(max_length=200), blank=True)
    level = models.IntegerField(default=10)

    def __str__(self):
        return self.word


class EnglishWord(models.Model):
    word = models.CharField(max_length=30)
    korean = models.ManyToManyField(KoreanWord)

    def __str__(self):
        return self.word

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    xp = models.IntegerField(default=0)

class History(models.Model):
    word = models.ForeignKey(EnglishWord, on_delete=models.CASCADE)
    success = models.BooleanField()
    Profil = models.ForeignKey(Profile, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)

class Accuracy(models.Model):
    word = models.ForeignKey(EnglishWord, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    correct_guesses = models.IntegerField(default=0)
    total_guesses = models.IntegerField(default=0)
    score = models.IntegerField(default=0)
