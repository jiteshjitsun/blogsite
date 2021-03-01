from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import BLANK_CHOICE_DASH
from django.forms.fields import DateTimeField
from django.urls import reverse


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')

class Post(models.Model):
    title = models.CharField(max_length=200)
    title_tag = models.CharField(max_length=20)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    # publish_date = models.DateField(auto_now_add=True)
    publish_time = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=200)
    likes = models.ManyToManyField(User, related_name='blog_post')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + ' | ' + str(self.writer)

    def get_absolute_url(self):
        return reverse('home')