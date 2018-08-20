from django.db import models


class Thread(models.Model):
    title = models.CharField(max_length=200)
    pub_name = models.CharField(max_length=20)
    pub_date = models.DateTimeField()
    content = models.TextField()
    life = models.DurationField()


class Post(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    pub_name = models.CharField(max_length=20)
    pub_date = models.DateTimeField()
    content = models.TextField()


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    pub_name = models.CharField(max_length=20)
    pub_date = models.DateTimeField()
    content = models.TextField()

