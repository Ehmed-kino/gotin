from django.db import models


class Word(models.Model):
    word_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    describtion = models.CharField(max_length=200)
    meaning = models.CharField(max_length=200)
    # votes = models.IntegerField(default=0)

    def __str__(self):
        return self.name