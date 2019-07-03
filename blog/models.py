from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_posted = models.DateTimeField(default=timezone.now)
    post_text = models.TextField(blank=True)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Comment(models.Model):
     author = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
     post = models.ForeignKey(Post, related_name='comments')
     comment_text = models.TextField()
     date_commented = models.DateTimeField(default=timezone.now)

     def __str__(self):
         return self.post