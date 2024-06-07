from django import forms

from .models import Perfil, Postagem, Comunidade#...

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

class NovoUsuarioForm(UserCreationForm):
  email = forms.EmailField()
  nome = forms.CharField(max_length=30)
  sobrenome = forms.CharField(max_length=30)
  
  username = forms.CharField(label='Nome de Usuário', required=True,
error_messages={
  'unique':'Este nome de usuário já está em uso.',
'required':'Este campo é obrigatóro'})
  
  password1 = forms.CharField(label='Senha', widget=forms.PasswordInput(
    attrs=({'class':'input-senha'})),
error_messages={'required':'Este campo é obrigatório'})
  
  password2 = forms.CharField(label='Confirme a Senha', widget=forms.PasswordInput,
error_messages={'required':'Por favor, confirme sua senha'})

  class Meta:
    model = User
    fields = ['username', 'nome', 'sobrenome', 'email',
    'password1', 'password2']

  
class LoginUsuarioForm(AuthenticationForm):
  username = forms.CharField(label='Nome de Usuário', widget=forms.TextInput(attrs={
    'class': 'form-control', 
    'placeholder': 'Usuário', 
    'id': 'id_username', 
    'autofocus': True,
    'autocapitalize': 'none',
    'autocomplete': 'username',
    'maxlength': '150'
    }))
  password = forms.CharField(label='Senha', widget=forms.PasswordInput(attrs={
    'class': 'form-control', 
    'placeholder': 'Senha',
    'autocomplete': 'current-password',
    'id': 'id_password'
    }))

#class PostagemForm (forms.ModelForm):
#  class Meta:
#    model = Postagem
#   fields = "__all__"
#   exclude = ["usuario"]
