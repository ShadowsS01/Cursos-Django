from django.contrib import admin
from .models import Cursos, Aulas, Comentarios, NotasAulas
from django.contrib.admin.decorators import display

@admin.register(Cursos)
class CursosAdm(admin.ModelAdmin):
    search_fields = ['nome',]

@admin.register(Aulas)
class AulasAdm(admin.ModelAdmin):
    list_display = ('nome', 'curso')
    search_fields = ['curso__nome', 'nome']

@admin.register(Comentarios)
class ComentariosAdm(admin.ModelAdmin):
    list_display = ('usuario', 'comentario', 'data', 'aula')
    search_fields = ['usuario__nome', 'aula__nome']

@admin.register(NotasAulas)
class NotasAulasAdm(admin.ModelAdmin):
    list_display = ('usuario', 'nota', 'aula')
    search_fields = ['usuario__nome', 'aula__nome']