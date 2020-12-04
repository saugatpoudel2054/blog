from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        'auth.User',
        on_delete = models.CASCADE
    )
    text = models.TextField()

    def __str__(self):
        return self.title[:50]
