from django.db import models
from django.utils import timezone

class Log(models.Model):
    user = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.title
