from django.db import models
from datetime import datetime
from django.contrib.auth.models import User 
from django.db.models import Model

class Perfil (models.Model):
  usuario =  models.ForeignKey(User, on_delete=models.CASCADE)
  user = models.CharField(max_length = 18)
  imagem = models.ImageField(blank = True, upload_to = 'pfp/')
  bio = models.CharField(max_length = 120)
  #def __str__(self):
  #  return self.usuario

class Postagem (models.Model):
  usuario =  models.ForeignKey(User, on_delete=models.CASCADE)
  texto = models.CharField(max_length = 280)
  imagem = models.ImageField(blank = True, upload_to = 'post_img/')
  data = models.DateTimeField(default=datetime.now)
  #def __str__(self):
  #  return self.data

class Comunidade (models.Model):
  nome = models.CharField(max_length = 18)
  desc = models.CharField(max_length = 180)


#fazer classe para respostas 