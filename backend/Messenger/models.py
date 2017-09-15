from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    online_code = models.CharField(max_length=200, default='offline')

    def __str__(self):
        return self.user.username


class TextMessage(models.Model):
    text_content = models.TextField()
    receiver = models.OneToOneField(UserProfile, related_name="receiver")
    sender = models.OneToOneField(UserProfile, related_name="sender")
