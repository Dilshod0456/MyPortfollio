from django.db import models

# Create your models here.
class Loyihalar(models.Model):
    title = models.CharField(max_length=50)
    discription = models.CharField(max_length=200)
    url = models.URLField()

    def __str__(self):
        return self.title

class Xabarlar(models.Model):
    fish = models.CharField(max_length=250)
    tell = models.CharField(max_length=13)
    email = models.EmailField()
    text = models.TextField()

    def __str__(self):
        return self.fish