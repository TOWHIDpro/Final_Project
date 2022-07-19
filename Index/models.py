from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Healthdata(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    age = models.FloatField()
    systolicbp = models.FloatField()
    diastolicbp = models.FloatField()
    bs = models.FloatField()
    heartRate = models.FloatField()
    message = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.user} || {self.date}"
