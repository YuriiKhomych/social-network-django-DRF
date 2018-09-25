from django.db import models
from django.conf import settings


class Post(models.Model):
    post_body = models.TextField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='author',
        on_delete=models.CASCADE
    )
    liked_by = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                      related_name='liked')
    added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.post_body} | {self.author} | {self.liked_by}'
