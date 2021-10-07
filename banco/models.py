from django.db import models

# Create your models here.

from peoples.models import People


class Agencia(models.Model):
    numero = models.IntegerField()

    def __str__(self):
        return str(self.numero)


class Conta(models.Model):
    numero = models.CharField(max_length=10)
    agencia = models.ForeignKey(Agencia, verbose_name=(
        "Agencia"), on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("Conta Corrente")
        verbose_name_plural = ("Contas Correntes")

    def __str__(self):
        return self.numero

    def get_absolute_url(self):
        return reverse("Conta_detail", kwargs={"pk": self.pk})


class Cliente(models.Model):

    pessoa = models.ForeignKey(People, on_delete=models.CASCADE)
    contas = models.ManyToManyField(Conta)

    def __str__(self):
        return self.pessoa

    def get_absolute_url(self):
        return reverse("Cliente_detail", kwargs={"pk": self.pk})
