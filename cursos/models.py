from django.db import models
from datetime import datetime
from usuarios.models import Usuario

class Cursos(models.Model):
    nome = models.CharField(max_length = 100)
    descricao = models.TextField()
    thumb = models.ImageField(upload_to = "thumb_cursos")

    class Meta:
        verbose_name_plural = 'Cursos'

    def __str__(self) -> str:
        return self.nome

class Aulas(models.Model):
    nome = models.CharField(max_length = 100)
    descricao = models.TextField()
    aula = models.FileField(upload_to = "aulas")
    curso = models.ForeignKey(Cursos, on_delete = models.CASCADE)

    class Meta:
        verbose_name_plural = 'Aulas'

    def __str__(self) -> str:
        return self.nome

class Comentarios(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete = models.CASCADE)
    comentario = models.TextField()
    data = models.DateTimeField(default = datetime.now)
    aula = models.ForeignKey(Aulas, on_delete = models.CASCADE)

    class Meta:
        verbose_name_plural = 'Comentarios'

    def __str__(self) -> str:
        return self.usuario.nome

class NotasAulas(models.Model):
    choices = (
        ('p', 'Péssimo'),
        ('r', 'Ruim'),
        ('re', 'Regular'),
        ('b', 'bom'),
        ('o', 'Ótimo')
    )

    class Meta:
        verbose_name_plural = 'Notas Aulas'

    aula = models.ForeignKey(Aulas, on_delete=models.CASCADE)
    nota = models.CharField(max_length=50, choices=choices)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)