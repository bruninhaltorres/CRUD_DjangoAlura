from django.contrib import admin
from app.models import Aluno, Curso, Matricula

class Alunos(admin.ModelAdmin):
    # Informações que serão disponibilizadas:
    list_display = ('id', 'nome', 'rg', 'data_nascimento')
    
    # Quando quer alterar pode clicar no id ou no nome
    list_display_links = ('id', 'nome')

    # Possibilita a busca por nome
    search_fields = ('nome',)

    # Caso tenham muitos alunos quero que sejam divididos em paginas
    list_per_page = 20

admin.site.register(Aluno, Alunos)

class Cursos(admin.ModelAdmin):

    list_display = ('id', 'codigo_curso', 'descricao')
    
    list_display_links = ('id', 'codigo_curso')

    search_fields = ('codigo_curso',)

admin.site.register(Curso, Cursos)

class Matriculas(admin.ModelAdmin):

    list_display = ('id', 'aluno', 'curso', 'periodo')
    
    list_display_links = ('id',)


admin.site.register(Matricula, Matriculas)

