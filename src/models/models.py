from django.db import models
from django.contrib.postgres.fields import ArrayField


class KoreanWord(models.Model):
    word = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    examples = ArrayField(models.CharField(max_length=200), blank=True)

    def __str__(self):
        return self.word


class EnglishWord(models.Model):
    word = models.CharField(max_length=30)
    korean = models.ManyToManyField(KoreanWord)

    def __str__(self):
        return self.word
