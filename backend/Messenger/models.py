from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    online_code = models.CharField(max_length=200, default='offline')

    def __str__(self):
        return self.user.username


class TextMessage(models.Model):
    text_content = models.TextField()
    receiver = models.ForeignKey(User, related_name="receiver", on_delete=models.CASCADE)
    sender = models.ForeignKey(User, related_name="sender", on_delete=models.CASCADE)
