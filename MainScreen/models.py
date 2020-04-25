from django.db import models
from django.contrib.auth.models import User

class User(models.Model):
    total = models.FloatField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.total