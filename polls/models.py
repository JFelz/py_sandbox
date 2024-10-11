from django.db import models

# Create your models here.
class Question(models.Model):
  question_text: str = models.CharField(max_length=200)
  PUBLICATION_DATE = models.DateTimeField("date published")


class Choice(models.Model):
  question: str = models.ForeignKey(Question, on_delete=models.CASCADE)
  choice_text: str = models.CharField(max_length=200)
  votes = models.IntegerField(default=0)
