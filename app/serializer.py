from rest_framework import serializers
from app.models import Aluno, Curso, Matricula


class AlunoSerializer(serializers.ModelSerializer):
    """Tranforma o tipo dos dados que já tenho no Models"""
    
    class Meta:
        model = Aluno

        # Filtro os dados que quero disponibilizar pra API:
        fields = ['id', 'nome', 'rg', 'data_nascimento']

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'

class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        fields = '__all__' # exclude = []

class ListaMatriculasAlunoSerializer(serializers.ModelSerializer):
    """Listagem dos cursos de um determinado aluno"""

    # Configuração para que na interface apareça a descrição do curso
    curso = serializers.ReadOnlyField(source = "curso.descricao")
    periodo = serializers.SerializerMethodField()

    class Meta:
        model = Matricula
        fields = ['curso', 'periodo']

    def get_periodo(self, obj):
        return obj.get_periodo_display()
    
class ListaAlunosDoCursoSerializer(serializers.ModelSerializer):
    """Listagem dos alunos de um cursos"""

    # Vai ler o campo nome nos Models
    aluno_nome = serializers.ReadOnlyField(source = "aluno.nome")

    class Meta:
        model = Matricula
        fields = ['aluno_nome']
