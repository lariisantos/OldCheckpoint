from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User

# Create your views here.
class SignupView(View):
    def get(self, req):
        return render(req, 'autenticacao/signup.html')
    
class SigninView(View):
    def get(self, req):
        return render(req, 'autenticacao/signin.html')