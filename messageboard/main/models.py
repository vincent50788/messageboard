from django.db import models
from django.utils import timezone
# Create your models here.
class Member(models.Model):
    user = models.CharField(max_length=100)#account name
    name = models.CharField(max_length=100)#user name
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class Message(models.Model):
    member = models.ForeignKey(Member)
    message = models.CharField(max_length=300)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.message
