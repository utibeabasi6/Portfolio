from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class Client(models.Model):
    name = models.CharField(max_length=500)
    logo = models.ImageField()

    def __str__(self) -> str:
        return self.name

class Work(models.Model):
    name = models.CharField(max_length=500)
    image = models.ImageField()
    category = models.CharField(max_length=300, choices=[
        ('web', 'Web'),
        ('mobile', 'Mobile'),
        ('design', 'Design')
    ])
    description = models.TextField()
    link = models.URLField(blank=True)
    contributions = ArrayField(models.CharField(max_length=500))
    client = models.CharField(max_length=500)

    def __str__(self) -> str:
        return self.name

class Review(models.Model):
    name = models.CharField(max_length=500)
    image = models.ImageField()
    review = models.TextField()

    def __str__(self) -> str:
        return self.name

class Skill(models.Model):
    name = models.CharField(max_length=500)
    proficiency = models.IntegerField()

    def __str__(self) -> str:
        return self.name

class Service(models.Model):
    name = models.CharField(max_length=500)
    description = models.TextField()
    icon = models.CharField(max_length=100)
    services = ArrayField(models.CharField(max_length=500))

    def __str__(self) -> str:
        return self.name