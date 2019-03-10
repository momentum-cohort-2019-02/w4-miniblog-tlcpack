from django.db import models
from django.urls import reverse




# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)

    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)

    description = models.TextField(max_length=10000, help_text='Start blogging!')

    date = models.DateField(auto_now_add=True)

    class Meta:
        # sorts by date
        ordering = ['date']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog-detail', args=[str(self.id)])


class Comment(models.Model):
    text = models.TextField(max_length=10000, help_text='Please add a friendly comment')

    author = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)

    date = models.DateField(auto_now_add=True)

class Author(models.Model):
    user_name = models.CharField(max_length=50)
    bio = models.CharField(max_length=5000)

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        return self.user_name

class User(models.Model):
    user_name = models.CharField(max_length=50)

    # comment = models.ForeignKey('Blog')

    def __str__(self):
        return self.user_name
