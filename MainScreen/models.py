from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Transaction(models.Model):
    value = models.FloatField()
    destination = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    transaction_user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.value

    def get_absolute_url(self):
        return reverse('transaction-detail', kwargs={'pk':self.pk})

