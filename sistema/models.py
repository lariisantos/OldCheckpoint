from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

#from django.contrib.postgres.fields import JSONField

# Create your models here.

class Game(models.Model):
    name = models.CharField(max_length=50) #A API tem q mandar pra esse models ok?
    imageUrl = models.CharField(max_length=200, default=False)
    platforms = models.JSONField(default=dict)
    likes = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Usuário')
    wishList = models.ManyToManyField(Game, related_name='wishlist')
    favorites = models.ManyToManyField(Game, related_name='Favorites')

    def __str__(self) -> str:
        return self.user.username

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    nota = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    #adicionar if caso game já tenha sido avaliado
#  - tnk