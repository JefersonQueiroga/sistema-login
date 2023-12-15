from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from rolepermissions.decorators import has_permission_decorator

@has_permission_decorator('nome_da_permissao')
def minha_view(request, *args, **kwargs):
    # Lógica da sua view
    ...

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                # Retorne uma mensagem de erro.
                return HttpResponse("Invalid username or password.")
    else:
        form = AuthenticationForm()

    return render(request, 'users/login.html', {'form': form})

from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    return redirect('login')

def index(request):
    return render(request, 'users/index.html')

@has_permission_decorator(['ADMINISTRADOR','GERENTE'])
def tela_admin(request):
    return render(request, 'users/admin.html')

@has_permission_decorator('gerente')
def tela_comum(request):
    return render(request, 'users/comum.html')