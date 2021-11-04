from django.shortcuts import render,redirect
from .models import Nota

def home(request):

    notas = Nota.objects.order_by('-created_at').all()
    dados = {
        'notas': notas
    }
    #Precisa enviar o request junto
    return render(request,'home.html', dados)


def about(request):
    #Precisa enviar o request junto
    return render(request,'about.html')

def buscar(request):
    if request.user.is_authenticated:
        notas = Nota.objects.order_by('-created_at').all()
    
        if 'search' in request.GET:
            nome_a_buscar = request.GET['search']
            if buscar:
                notas = notas.filter(nome_nota__icontains=nome_a_buscar)
        dados = {
            'notas': notas
        }
        #Precisa enviar o request junto
        return render(request,'index.html', dados)
    else:
        return redirect('login')

    