from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth, messages
from notas.models import Nota


def cadastro(request):
    if request.method == 'POST':
        # is_private = request.POST.get('is_private', False)
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirmpassword')
        if not name.strip():
            messages.error(request, 'O nome não pode ficar em branco')
            return redirect('cadastro')
        if not email.strip():
            messages.error(request, 'O email não pode ficar em branco')
            return redirect('cadastro')
        if password != confirm_password:
            messages.error(request, 'As senhas não são iguais!')
            return redirect('cadastro')
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Usuario já cadastrado')
            return redirect('cadastro')
        user = User.objects.create_user(
            username=name, email=email, password=password)
        user.save()
        messages.success(request, 'Cadastro realizado')

        print(user)
        return redirect('login')
    else:
        return render(request, 'cadastro.html')


def login(request):
    if request.method == 'POST':
        # is_private = request.POST.get('is_private', False)
        email = request.POST.get('email')
        password = request.POST.get('password')
        if email == "" or password == "":
            print("Os campos não podem ficar em branco")
            return redirect('login')
        if User.objects.filter(email=email).exists():
            # Pegando apena so username
            name = User.objects.filter(email=email).values_list(
                'username', flat=True).get()
            print("name", name)
            user = auth.authenticate(request, username=name, password=password)
            if user is not None:
                auth.login(request, user)
                print("Login realizado com sucesso")
                return redirect('dashboard')
    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('home')


def dashboard(request):
    if request.user.is_authenticated:
        id = request.user.id
        print("------test------")
        print(request.user.id)
        print(id)
        notas = Nota.objects.order_by('-created_at').filter(user=id)

        dados = {
            'notas': notas
        }
        return render(request, 'index.html', dados)
    else:
        return redirect('login')


def cria_nota(request):
    print("--------teste----------")
    if request.method == 'POST':
        title_nota = request.POST.get('title_nota')
        category_nota = request.POST.get('category_nota')
        content_nota = request.POST.get('content_nota')
        user = get_object_or_404(User, pk=request.user.id)
        nota = Nota.objects.create(
            user=user, nome_nota=title_nota, category=category_nota, content=content_nota)
        nota.save()
        return redirect('dashboard')
    else:
        return redirect('dashboard')


def delete_nota(request, nota_id):
    nota = get_object_or_404(Nota, pk=nota_id)
    nota.delete()
    messages.success(request, 'Nota deletada')

    return redirect('dashboard')


def edit_nota(request):
    if request.method == 'POST':
        nota_id = request.POST.get('nota_id') 

        nota = Nota.objects.get(pk=nota_id)

        nota.nome_nota = request.POST.get('title_nota')
        nota.category = request.POST.get('category_nota')
        nota.content = request.POST.get('content_nota')

        nota.save()
        return redirect('dashboard')
    else:
        return redirect('dashboard')

    