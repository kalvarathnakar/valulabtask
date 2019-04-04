from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(blank=True,null=True)
    created_date = models.DateTimeField(default=timezone.now)
    track_name = models.ForeignKey('Track',on_delete=models.CASCADE)
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    answer_status = models.CharField(max_length=100)
    def __str__(self):
        return self.choice_text

class Track(models.Model):
    name = models.CharField(max_length=200)
    #question = models.ForeignKey(Question,blank=True null=True)
    def __str__(self):
        return self.name
class QuestionAnswer(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    answer_status = models.CharField(max_length=200)