from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


# Creating a model for the Post
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    # After Creating the Post Need to redirect to the Detail Post Template
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={ 'pk': self.pk })