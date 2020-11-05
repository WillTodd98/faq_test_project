from django.db import models

# Create your models here.

class Question(models.Model):
    question_text = models.TextField()
    answer_text = models.TextField()
    answered = models.BooleanField(default='False')

    def get_absolute_url(self):
        return f"http://127.0.0.1:8000/questions/{self.id}/"