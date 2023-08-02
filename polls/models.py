import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    '''
    Question entity with the question and the publishing date
    '''

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self) -> str:
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    '''
    Choice entity with a one to one relationship with the Question
    entiry. It also has a choice options and a tally of votes cast
    '''
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.choice_text