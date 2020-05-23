from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Transaction(models.Model):

    class Transaction_Direction(models.IntegerChoices):
        SEND = 1
        RECEIVE = 2

    class Transaction_Type(models.IntegerChoices):
        ENTERTAINMENT = 1
        UTILITIES = 2
        FOOD = 3
        TRANSPORT = 4

    value = models.FloatField()
    destination = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    transaction_user = models.ForeignKey(User, on_delete=models.CASCADE)
    transaction_type = models.IntegerField(choices=Transaction_Type.choices)
    transaction_direction = models.IntegerField(choices=Transaction_Direction.choices)

    def __str__(self):
        return self.value

    def get_absolute_url(self):
        return reverse('transaction-detail', kwargs={'pk':self.pk})

