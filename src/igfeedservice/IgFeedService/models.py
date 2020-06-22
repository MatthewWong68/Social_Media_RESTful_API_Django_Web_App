from django.db import models

# Create your models here.

class Post(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    full_text = models.CharField(max_length=8191)
    crawled_dt = models.DateTimeField(auto_now=False)
    post_dt = models.DateTimeField(auto_now=False)
    author_name = models.CharField(max_length=255)
    like = models.IntegerField(default=0)
    comment = models.IntegerField(default=0)

    def __str__(self):
        return self.id

# class PostHistory(Post):
#     post = ForeignKey(Post) 

class Page(models.Model):
    id = models.AutoField(primary_key=True)
    author_name = models.CharField(max_length=255)
    posts = models.IntegerField(default=0)
    followers = models.IntegerField(default=0)
    following = models.IntegerField(default=0)

    def __str__(self):
        return self.id

class Hashtag(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.CharField(max_length=255)
    feedID = models.CharField(max_length=20)

    def __str__(self):
        return self.id