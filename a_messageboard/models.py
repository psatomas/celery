from django.db import models
from django.contrib.auth.models import User    
class MessageBoard(models.Model):
    subscribers = models.ManyToManyField(User, related_name='messageboard', blank=True)

    def __str__(self):
        return str(self.id)
    
