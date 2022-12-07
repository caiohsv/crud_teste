from django.db import models
from django.contrib.auth import get_user_model


class Livros(models.Model):
    nome = models.CharField(max_length=50)
    autor = models.CharField(max_length=50)
    genero = models.CharField(max_length=50)

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nome
