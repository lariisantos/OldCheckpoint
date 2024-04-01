from django.shortcuts import render
from django.views import View

# Create your views here.
class selectedGameView(View):
    def get(self, req):
        return render(req, 'sistema/pagjogo.html')
    

