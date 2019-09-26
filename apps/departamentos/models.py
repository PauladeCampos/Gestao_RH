from django.db import models

# Crie seu modelo aqui.
class Departamento(models.Model):
    nome = models.CharField(max_length=70)

    def __str__(self):
        return self.nome