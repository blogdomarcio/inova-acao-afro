from django.db import models

# Create your models here.
from django.urls import reverse


class Estado(models.Model):

    sigla = models.CharField(max_length=2, unique=True)

    def __str__(self):
        return self.sigla


class Cidade(models.Model):

    nome = models.CharField(max_length=150)
    uf = models.ForeignKey(Estado, on_delete=models.CASCADE)


    def __str__(self):
        return self.nome

class Bairro(models.Model):
    nome = models.CharField(max_length=150)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Cartorio(models.Model):
    nome_fantasia = models.CharField(max_length=150, null=True, blank=True)
    nome_oficial = models.CharField(max_length=150, null=True, blank=True)
    cnpj = models.CharField(max_length=18, null=True, blank=True)
    cns = models.CharField(max_length=8, null=True, blank=True)

    titular = models.CharField(max_length=50, null=True, blank=True)
    substituto = models.CharField(max_length=50, null=True, blank=True)
    juiz = models.CharField(max_length=50, null=True, blank=True)

    endereco = models.CharField(max_length=100, null=True, blank=True)
    cep = models.CharField(max_length=8, null=True, blank=True)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, null=True, blank=True)
    bairro = models.ForeignKey(Bairro, on_delete=models.CASCADE, null=True, blank=True)

    telefone = models.CharField(max_length=50, null=True, blank=True)
    fax = models.CharField(max_length=50, null=True, blank=True)
    homepage = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    observacao = models.CharField(max_length=100, null=True, blank=True)
    horario = models.CharField(max_length=100, null=True, blank=True)
    abrangencia = models.CharField(max_length=100, null=True, blank=True)
    atribuicoes = models.CharField(max_length=200, null=True, blank=True)
    comarca = models.CharField(max_length=100, null=True, blank=True)
    entrancia = models.CharField(max_length=100, null=True, blank=True)

    data_inst = models.DateField(null=True, blank=True)
    data_ult_atual  = models.DateField(null=True, blank=True)

    ativo = models.BooleanField(default=True)

    def __str__(self):
        return str(self.nome_oficial) + ' - ' + str(self.cidade).upper()
