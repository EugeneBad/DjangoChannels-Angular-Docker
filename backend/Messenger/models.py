from django.db import models
from django.conf import settings


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    online_code = models.CharField(max_length=200, default='offline')


class TextMessage(models.Model):
    text_content = models.TextField()
    receiver = models.OneToOneField(UserProfile, related_name="receiver")
    sender = models.OneToOneField(UserProfile, related_name="sender")
