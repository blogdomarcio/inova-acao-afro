from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.views import APIView

from cartorio.api.serializers import EstadosSerializer, CidadesSerializer, CartoriosSerializer
from cartorio.models import Estado, Cidade, Cartorio


def index(request):
    usuario = User.objects.get(id=request.user.id)
    cartorios = Cartorio.objects.count()
    cidades = Cidade.objects.count()
    estados = Estado.objects.count()


    context = {
        'usuario': usuario,
        'cartorios': cartorios,
        'estados': estados,
        'cidades': cidades,
    }

    return render(request, 'cartorio/index.html', context)


def estados(request):
   estados = Estado.objects.all()
   usuario = User.objects.get(id=request.user.id)

   context = {
       'estados': estados,
       'usuario': usuario,
   }

   return render(request, 'cartorio/estados.html', context)


def estado(request, estado):

   estado = Estado.objects.get(sigla=estado)
   cidades = Cidade.objects.filter(uf=estado)
   usuario = User.objects.get(id=request.user.id)

   context = {
       'cidades': cidades,
       'usuario': usuario,
       'estado': estado,
   }

   return render(request, 'cartorio/cidades.html', context)


def cidade(request, cidade):

    cidade = Cidade.objects.get(id=cidade)
    cartorios = Cartorio.objects.filter(cidade=cidade)

    usuario = User.objects.get(id=request.user.id)

    context = {
        'cartorios': cartorios,
        'usuario': usuario,
        'cidade': cidade,
    }

    return render(request, 'cartorio/cartorios.html', context)


def catorio_detalhe(request, cartorio):
    cartorio = Cartorio.objects.get(id=cartorio)

    usuario = User.objects.get(id=request.user.id)

    context = {
        'cartorio': cartorio,
        'usuario': usuario,
    }

    return render(request, 'cartorio/cartorio_detalhe.html', context)


# class ListEstados(APIView):
#     def get(self, request):
#         estados = EstadosSerializer
#
#         return Response(estados)


@api_view(['GET'])
@renderer_classes([JSONRenderer])
def lista_estados(request):
    estados = Estado.objects.all()
    serializer = EstadosSerializer(estados, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@renderer_classes([JSONRenderer])
def lista_cidades_estado(request, estado):
    estado = Estado.objects.get(sigla=estado)
    cidades = Cidade.objects.filter(uf=estado.id)
    serializer = CidadesSerializer(cidades, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@renderer_classes([JSONRenderer])
def lista_cartorios_cidade(request, cidade):
    cidade = Cidade.objects.get(id=cidade)
    cartorios = Cartorio.objects.filter(cidade=cidade)
    serializer = CartoriosSerializer(cartorios, many=True)
    return Response(serializer.data)