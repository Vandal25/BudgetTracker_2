from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models import Sum

class Transaction(models.Model):

    class Transaction_Direction(models.IntegerChoices):
        SEND = 1
        RECEIVE = 2

    class Transaction_Type(models.IntegerChoices):
        DEFAULT = 1
        ENTERTAINMENT = 2
        UTILITIES = 3
        FOOD = 4
        TRANSPORT = 5

    value = models.FloatField()
    destination = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    transaction_user = models.ForeignKey(User, on_delete=models.CASCADE)
    transaction_type = models.IntegerField(default=1, choices=Transaction_Type.choices)
    transaction_direction = models.IntegerField(default=1, choices=Transaction_Direction.choices)

    def get_absolute_url(self):
        return reverse('transaction-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.value



