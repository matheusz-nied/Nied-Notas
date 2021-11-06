from django.shortcuts import render,redirect
from .models import Nota

def home(request):
    #Precisa enviar o request junto
    return render(request,'home.html')


def about(request):
    #Precisa enviar o request junto
    return render(request,'about.html')

def buscar(request):
    if request.user.is_authenticated:
        id = request.user.id
        notas = Nota.objects.order_by('-created_at').filter(user=id)
    
        if 'search' in request.GET:
            nome_a_buscar = request.GET.get('search')
            if buscar:
                notas = notas.filter(nome_nota__icontains=nome_a_buscar)
        dados = {
            'notas': notas
        }
        #Precisa enviar o request junto
        return render(request,'index.html', dados)
    else:
        return redirect('login')

    