from django.db import models

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=50)
    answerA = models.CharField(max_length=50)
    answerB = models.CharField(max_length=50)
    
    def __str__(self):
        return self.title