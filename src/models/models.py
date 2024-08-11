from django.db import models


class KoreanWord(models.Model):
    word = models.CharField(max_length=20)
    description = models.TextField()
    examples = models.TextField()

    def __str__(self):
        return self.word


class EnglishWord(models.Model):
    word = models.CharField(max_length=30)
    korean = models.ManyToManyField(KoreanWord)

    def __str__(self):
        return self.word
