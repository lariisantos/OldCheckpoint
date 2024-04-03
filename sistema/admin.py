from django.contrib import admin
from .models import Game
from .models import Profile
from .models import Rating

# Register your models here.
admin.site.register(Game)
admin.site.register(Profile)
admin.site.register(Rating)

# us

# Rating.objects.create(user)