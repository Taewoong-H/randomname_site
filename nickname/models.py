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

#각각의 카테고리 저장해두기
class Index(models.Model):
    name = models.CharField(max_length=50)
    num = models.IntegerField(default=0)

    def __str__(self):
        return self.name
         
    