from django.db import models


class Livros(models.Model):
    nome = models.CharField(max_length=50)
    autor = models.CharField(max_length=50)
    genero = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
