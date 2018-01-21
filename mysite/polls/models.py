from django.db import models

# Create your models here.

class Queation(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date publisted')

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Queation, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text