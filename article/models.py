from django.db import models

# Create your models here.
class Author(models.Model):
  name = models.CharField(max_length=255)
  email = models.EmailField()

  def __str__(self):
        return self.name

class Article(models.Model):
  title = models.CharField(max_length=120)
  body = models.TextField()

  def __str__(self):
    return self.title