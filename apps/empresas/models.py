from django.db import models


# Crie seus modelo aqui.
class Empresa(models.Model):
    nomeFantasia = models.CharField(max_length = 100,help_text = 'Nome Fantasia da Empresa')

    def __str__(self):
        return self.nomeFantasia
