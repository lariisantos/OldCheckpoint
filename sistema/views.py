from django.shortcuts import render, redirect
from django.views import View

# Create your views here.
class selectedGameView(View):
    def get(self, req):
        if(req.user.is_authenticated):
            return render(req, 'sistema/pagjogo.html')
        
        return redirect('/')
    
#class gameRating(View):
#    def post(self, req(?), jogoId, usuarioId):
        #instanceJogo = Game(pk= jogoId)
    
        # newRating = instance.Jogo 
        #instance.save()
        # return newValueForRating


    
    