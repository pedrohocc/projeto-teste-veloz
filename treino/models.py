from django.db import models

# Create your models here.
class Treino(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    data = models.DateField()
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome