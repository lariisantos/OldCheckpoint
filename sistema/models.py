from django.db import models
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Game(models.Model):
    name = models.CharField(max_length=50) #A API tem q mandar pra esse models ok?
    imageUrl = models.CharField(max_length=200, default=False)
    platforms = models.JSONField(default=dict)
    likes = models.IntegerField(default=0)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Usuário')
    wishList = models.ManyToManyField(Game, related_name='wishlist')
    favorites = models.ManyToManyField(Game, related_name='favorites')
