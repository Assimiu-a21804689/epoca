from django.db import models

class Contacto (models.Model):
    nome = models.CharField(max_length=40)
    apelido = models.CharField(max_length=40)
    telefone = models.CharField(max_length=9)
    imail = models.EmailField()
    dataNascimento = models.DateField()

class Quizz(models.Model):
    o = models
