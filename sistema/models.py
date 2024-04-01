from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.db import models

# Create your models here.

from django.apps import AppConfig


class game(models.Model):
    name = models.CharField(max_length=50) #A API tem q mandar pra esse models ok?
    #plataformas???

class usuario(models.Model):
    userName = models.CharField(max_length=50)
    dataDeGamesDoUser = game # cada user vai ter seu dado de games(?)
    #wishlist array

