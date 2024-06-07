from django.contrib import admin
from .models import Comunidade, Perfil, Postagem, Comunidade#...

#colocar os registros do models aqui

class PerfilAdmin(admin.ModelAdmin):
 list_display = ['usuario', 'bio']
 ordering = ['usuario','bio']
 list_filter = ['usuario']

class PostagemAdmin(admin.ModelAdmin):
 list_display = ['usuario', 'texto']
 ordering = ['usuario','texto']
 list_filter = ['usuario']

admin.site.register(Perfil, PerfilAdmin)
admin.site.register(Postagem, PostagemAdmin)
admin.site.register(Comunidade)

