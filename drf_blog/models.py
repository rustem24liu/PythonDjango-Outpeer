from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False, verbose_name='Title')
    description = models.TextField(null=False, blank=False, verbose_name='Description')
    author = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Author', related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated at')

    def __str__(self):
        return f'{self.pk} - {self.title}'


class Comment(models.Model):
    text = models.TextField(null=False, blank=False, verbose_name='Comment')
    author = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Author', related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated at')
    post = models.ForeignKey(Post, on_delete=models.PROTECT, verbose_name='Post', related_name='comments')

    def __str__(self):
        return f'{self.pk} - {self.text[:20]} by {self.author}'
