from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    rfid = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Question(models.Model):
    title = models.CharField(max_length=100)
    question = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

class UserAnswer(models.Model):
    ANSWER_CHOICES = [
        ('za', 'Za'),
        ('przeciw', 'Przeciw'),
        ('wstrzymal sie', 'Wstrzymał się'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=20, choices=ANSWER_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
