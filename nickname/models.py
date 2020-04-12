from django.db import models

# Create your models here.
class Animal(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Adjective(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Food(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
         
    