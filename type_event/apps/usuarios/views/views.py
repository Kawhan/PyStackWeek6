from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.shortcuts import redirect, render
from django.urls import reverse
from usuarios.utils.utils import verificar_senha_forte


# Create your views here.
def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        if not (senha == confirmar_senha):
            messages.add_message(request, constants.ERROR,
                                 'Suas senhas não coincidem.')
            return redirect(reverse('cadastro'))

        user = User.objects.filter(username=username)

        if user.exists():
            messages.add_message(
                request, constants.ERROR, 'Já existe uma conta registrada com esses dados!')
            return redirect(reverse('cadastro'))

        if not (verificar_senha_forte(senha)):
            messages.add_message(
                request, constants.ERROR, 'Suas senhas é fraca, por favor digitar entre 1 a 8 digitos, com caracteres especiais e pelo menos 1 letra maiuscula!')
            return redirect(reverse('cadastro'))

        user = User.objects.create_user(
            username=username, email=email, password=senha)
        user.save()
        messages.add_message(request, constants.SUCCESS,
                             'Conta criada com sucesso.')
        return redirect(reverse('login'))


def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = auth.authenticate(username=username, password=senha)

        if not user:
            messages.add_message(request, constants.ERROR,
                                 'Username ou senha inválidos')
            return redirect(reverse('login'))

        auth.login(request, user)
        return redirect('novo_evento')
