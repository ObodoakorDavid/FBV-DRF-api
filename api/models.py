from msilib.schema import Class
from django.db import models

# Create your models here.

class Chat(models.Model):
    username = models.TextField(max_length=50)
    message = models.TextField(max_length=200)
    time_sent = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.username