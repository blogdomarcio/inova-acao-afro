from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.generics import get_object_or_404
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.views import APIView

from cartorio.api.serializers import EstadosSerializer, CidadesSerializer, CartoriosSerializer
from cartorio.models import Estado, Cidade, Cartorio


@login_required
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


@login_required
def estados(request):
    estados = Estado.objects.all()
    usuario = User.objects.get(id=request.user.id)

    context = {
        'estados': estados,
        'usuario': usuario,
    }

    return render(request, 'cartorio/estados.html', context)


@login_required
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


@login_required
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


@login_required
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


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
@renderer_classes([JSONRenderer])
def api_cartorio(request, cartorio):
    try:
        cartorio = Cartorio.objects.get(id=cartorio)
    except Cartorio.DoesNotExist:
        return JsonResponse({'message': 'Cartorio inexistente'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':

        serializer = CartoriosSerializer(cartorio, many=False)

        return Response(serializer.data)

    elif request.method == 'POST':
        cartorio_data = JSONParser().parse(request)
        cartorio_serializer = CartoriosSerializer(data=cartorio_data)
        if cartorio_serializer.is_valid():
            cartorio_serializer.save()
            return JsonResponse(cartorio_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(cartorio_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':

        cartorio.delete()
        return JsonResponse({'message': 'Cart??rio exclu??do com sucesso!'})

    elif request.method == 'PUT':
        cartorio_data = JSONParser().parse(request)
        cartorio_serializer = CartoriosSerializer(cartorio, data=cartorio_data)
        if cartorio_serializer.is_valid():
            cartorio_serializer.save()
            return JsonResponse(cartorio_serializer.data)
        return JsonResponse(cartorio_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    elif request.method == 'PATCH':
        cartorio_data = JSONParser().parse(request)
        cartorio_serializer = CartoriosSerializer(cartorio, data=cartorio_data)
        if cartorio_serializer.is_valid():
            cartorio_serializer.save()
            return JsonResponse(cartorio_serializer.data)
        return JsonResponse(cartorio_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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


def cidades(request):
    usuario = User.objects.get(id=request.user.id)

    cidades = Cidade.objects.all().order_by('nome')

    paginator = Paginator(cidades, 500)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'cidades': page_obj,
        'usuario': usuario,
    }

    return render(request, 'cartorio/listacidades.html', context)


def cartorios(request):
    usuario = User.objects.get(id=request.user.id)

    cartorios = Cartorio.objects.all().order_by('nome_oficial')

    paginator = Paginator(cartorios, 500)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'cartorios': page_obj,
        'usuario': usuario,
    }

    return render(request, 'cartorio/listacartorios.html', context)


@api_view(['GET'])
@renderer_classes([JSONRenderer])
def lista_cartorios_estado(request, estado):
    try:
        estado = Estado.objects.get(sigla=estado)

    except Estado.DoesNotExist:

        return JsonResponse({'message': 'Estado inexistente'}, status=status.HTTP_404_NOT_FOUND)

    cartorios = Cartorio.objects.filter(cidade__uf=estado.id)

    paginator = LimitOffsetPagination()
    result_page = paginator.paginate_queryset(cartorios, request)
    serializer = CartoriosSerializer(result_page, many=True)

    return paginator.get_paginated_response(serializer.data)


@api_view(['POST', 'GET', ])
@renderer_classes([JSONRenderer])
def add_cartorio(request):
    if request.method == 'GET':
        cartorios = Cartorio.objects.all()
        paginator = LimitOffsetPagination()
        result_page = paginator.paginate_queryset(cartorios, request)
        serializer = CartoriosSerializer(result_page, many=True)

        return paginator.get_paginated_response(serializer.data)

    if request.method == 'POST':
        cartorio_data = JSONParser().parse(request)
        cartorio_serializer = CartoriosSerializer(data=cartorio_data)
        if cartorio_serializer.is_valid():
            cartorio_serializer.save()
            return JsonResponse(cartorio_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(cartorio_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
