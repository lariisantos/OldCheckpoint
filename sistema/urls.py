from django.contrib import admin
from django.urls import path, include
from . import views
#from .views import SelectedGameView


urlpatterns = [
    path('', views.selectedGameView.as_view(), name='gameView')
]