from django.db import models

# Crie seus modelos aqui.

class Funcionario(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
