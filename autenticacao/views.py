from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib import auth

# Create your views here.
class SignupView(View):
    def get(self, req):
        if(req.user.is_authenticated):
            return redirect('/app')
        
        return render(req, 'autenticacao/signup.html')

    def post(self, req):
        username = req.POST.get('username')
        email = req.POST.get('email')
        password = req.POST.get('password')
        c_password = req.POST.get('c-password')

        user = User.objects.filter(username=username)

        if(user.exists()):
            messages.add_message(req, constants.ERROR, 'Username já existe!')
        else:
            if(password != c_password):
                messages.add_message(req, constants.ERROR, 'As senhas não são iguais!')
            else:
                user = User.objects.create_user(username=username, password=password, email=email)
                user.save()

                return redirect('/')

        return render(req, 'autenticacao/signup.html')


    
class SigninView(View):
    def get(self, req):
        if(req.user.is_authenticated):
            return redirect('/app')
        
        return render(req, 'autenticacao/signin.html')
    
    def post(self, req):
        username = req.POST.get('username')
        password = req.POST.get('password')

        USER = auth.authenticate(username=username, password=password)

        if not USER:
            messages.add_message(req, constants.ERROR, 'Email ou senha inválidos')
            return render(req, 'autenticacao/signin.html')
        else:
            auth.login(req, USER)
            return redirect('/app')