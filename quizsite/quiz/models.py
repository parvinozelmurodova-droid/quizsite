from django.db import models


class Question(models.Model):
    text = models.CharField(max_length=300)
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)

    correct_answer = models.CharField(max_length=200)

    explanation = models.TextField()
    link = models.URLField()

    def __str__(self):
        return self.text
