from django.urls import path
from . import views

app_name = 'autenticacao'

urlpatterns = [
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('', views.SigninView.as_view(), name='signin'),
]