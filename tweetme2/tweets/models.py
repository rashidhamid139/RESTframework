import random
from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL
# Create your models here.


class TweetLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.ForeignKey("Tweet", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

class Tweet(models.Model):

    parent = models.ForeignKey("self", null=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(null=True, blank=True)
    likes = models.ManyToManyField(User, related_name='tweet_user', blank=True, through=TweetLike)
    image = models.FileField(upload_to='images/', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content

    @property
    def is_retweet(self):
        return self.parent != None

    def serialize(self):
        return {
            "id": self.id,
            "content": self.content,
            "likes": random.randint(1,99)
        }

    class Meta:
        ordering = ["-id"]
