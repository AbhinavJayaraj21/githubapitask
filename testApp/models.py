from django.db import models

# Create your models here.


class Repository(models.Model):
    name = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
    description = models.TextField(null=True)
    stars = models.IntegerField()
    forks = models.IntegerField()

    def __str__(self):
        return self.name
