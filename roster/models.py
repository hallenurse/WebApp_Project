from django.db import models
from django.config import settings
from django.contrib.auth import get_user_model
from django.urls import reverse

class Roster(models.Model):
    name = models.CharFiled(max_length=200)
    number = models.PositiveSmallIntegerField()
    position = models.TextField()
    bio = models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('player_detail', args=[str(self.id)])
    
