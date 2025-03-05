from django.db import models

class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    birthdate = models.DateField()
class Dreams(models.Model):
    user =models.ForeignKey(Users)
    dream = models.TextField()
    dream_interpreted = models.TextField()
    share = models.BooleanField()
class WordDictionary(models.Model):
    user = models.ForeignKey(Users)
    word = models.CharField(max_length=255)
    count = models.IntegerField()

