from django.contrib.auth.models import User
from django.shortcuts import render


# Create your views here.
from banco.models import Agencia


def index(request):

    usuario = User.objects.get(id=request.user.id)

    agencias = Agencia.objects.count()

    context = {
        'usuario': usuario,
        'agencias': agencias,
    }

    return render(request, 'people/dashboard/banco/index.html', context)

def lista(request):
    usuario = User.objects.get(id=request.user.id)
    agencias = Agencia.objects.all()

    context = {
        'usuario': usuario,
        'agencias': agencias,
    }

    return render(request, 'people/dashboard/banco/agencias.html', context)
