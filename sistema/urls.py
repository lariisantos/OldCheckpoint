from django.contrib import admin
from django.urls import path, include
from . import views
#from .views import SelectedGameView

app_name = "sistema"

urlpatterns = [
    path('', views.selectedGameView.as_view(), name='gameView')
]

