from django.shortcuts import render, redirect, get_object_or_404

from .forms import NovoUsuarioForm, LoginUsuarioForm
#from .forms import PostagemForm
from .models import Comunidade, Perfil, Postagem#, Comunidade...
3
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

#ainda tem que fazer o migrate
def start(request):
  return render(request,'start.html')

@login_required
def home(request):
  perfil = Perfil.objects.all()
  post = Postagem.objects.all().order_by('-data')
  comunidade = Comunidade.objects.all()
  #user = Perfil.objects.filter(perfil=request.user.id)
#talvez algo esteja errado embaixo
  return render(request, 'home.html',  context={"comunidades": comunidade,
                                                "perfil": perfil,
                                                "post": post})

def cadastro_usuario(request):
  formulario = NovoUsuarioForm()
  if request.method == 'POST' and request.POST:
    formulario = NovoUsuarioForm(request.POST)
    if formulario.is_valid():
      novo_usuario = formulario.save(commit=False)
      novo_usuario.email = formulario.cleaned_data['email']
      novo_usuario.first_name = formulario.cleaned_data['nome']
      novo_usuario.last_name = formulario.cleaned_data['sobrenome']
      novo_usuario.save() 
      print('Conta criada com sucesso')
      return redirect('/login')
  return render(request,'cadastro.html',
               {'formulario': formulario})


def login_usuario (request):
  formulario = LoginUsuarioForm()
  if request.method == 'POST' and request.POST:
    formulario = LoginUsuarioForm(request, request.POST)
    if formulario.is_valid():
      usuario = formulario.get_user()
      login(request, usuario)
      return redirect('/home')
  return render(request, 'login.html', {'formulario': formulario}) 

def logout_usuario(request):
  logout(request)
  return redirect('/home')

def sobre(request):
  return render(request, 'sobre.html')

@login_required
def feed(request):
  return render(request, 'feed.html')
