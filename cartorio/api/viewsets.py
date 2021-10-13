from rest_framework import viewsets

from cartorio.api.serializers import EstadosSerializer, CidadesSerializer, CartoriosSerializer
from cartorio.models import Estado, Cartorio, Cidade


class EstadosViewSet(viewsets.ModelViewSet):
    queryset = Estado.objects.all()
    serializer_class = EstadosSerializer


class CidadesViewSet(viewsets.ModelViewSet):
    queryset = Cidade.objects.all()
    serializer_class = CidadesSerializer


class CartoriosViewSet(viewsets.ModelViewSet):
    queryset = Cartorio.objects.all()
    serializer_class = CartoriosSerializer