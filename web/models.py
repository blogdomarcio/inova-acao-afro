from django.db import models

from util.util import generate_nome


class Curriculo(models.Model):
    nome = models.CharField(max_length=150)
    profissao = models.CharField(max_length=150, null=True, blank=True)
    phone = models.CharField(max_length=14, null=True, blank=True)
    email = models.EmailField(max_length=50,  null=True, blank=True)
    facebook = models.CharField(max_length=50,  null=True, blank=True)
    linkedin = models.CharField(max_length=50,  null=True, blank=True)
    insta = models.CharField(max_length=50,  null=True, blank=True)
    youtube = models.CharField(max_length=50, null=True, blank=True)
    twitter = models.CharField(max_length=50, null=True, blank=True)
    about = models.TextField(null=True)
    age = models.IntegerField()
    adress = models.CharField(max_length=100, null=True, blank=True)
    language = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.nome


class Skill(models.Model):
    person = models.ForeignKey(Curriculo, on_delete=models.PROTECT, null=True, blank=True)
    percetenge = models.IntegerField()
    description = models.CharField(max_length=150)

    def __str__(self):
        return str(self.description) + '-' + str(self.percetenge) + '%'

class Education(models.Model):
    person = models.ForeignKey(Curriculo, on_delete=models.PROTECT, null=True, blank=True)
    curso = models.CharField(max_length=150)
    school = models.CharField(max_length=150)
    description = models.TextField()
    sigla = models.CharField(max_length=50)
    start = models.CharField(max_length=50)
    end = models.CharField(max_length=50)

    def __str__(self):
        return self.curso


class Experience(models.Model):
    person = models.ForeignKey(Curriculo, on_delete=models.PROTECT, null=True, blank=True)
    titulo = models.CharField(max_length=150, null=True, blank=True)
    description = models.TextField()
    empresa = models.CharField(max_length=150, null=True, blank=True)
    start = models.CharField(max_length=50, null=True, blank=True)
    end = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.titulo

class Portifolio(models.Model):
    person = models.ForeignKey(Curriculo, on_delete=models.PROTECT, null=True, blank=True)
    titulo = models.CharField(max_length=150, null=True, blank=True)

    CAT_CHOICES = [
        ("Graphic", "Graphic"),
        ("Web", "Web"),
        ("Photo", "Photo"),
    ]

    categoria = models.CharField(max_length=10, choices=CAT_CHOICES)

    imagem = models.ImageField(upload_to=generate_nome, null=True, blank=True)
     
    description = models.TextField(blank=True)
    empresa = models.CharField(max_length=150, null=True, blank=True)
    start = models.CharField(max_length=50, null=True, blank=True)
    end = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.titulo

class Mensagem(models.Model):
    nome = models.CharField(max_length=150, null=True, blank=True)
    email = models.EmailField(max_length=100)
    assunto =  models.CharField(max_length=100, null=True, blank=True)
    mensagem = models.TextField(blank=True)
    data_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome