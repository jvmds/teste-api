from django.db import models


class Saida(models.Model):

    acao = models.CharField(max_length=400)
    paReq = models.CharField(max_length=1000)
    termUrl = models.CharField(max_length=1000)
    md = models.CharField(max_length=1000)


class Entrada(models.Model):

    md = models.CharField(max_length=1000)
    pares = models.CharField(max_length=1000)