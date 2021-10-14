from rest_framework import viewsets, pagination

from cartorio.api.serializers import EstadosSerializer, CidadesSerializer, CartoriosSerializer
from cartorio.models import Estado, Cartorio, Cidade


class CustomPagination(pagination.PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 50
    page_query_param = 'p'


class EstadosViewSet(viewsets.ModelViewSet):
    queryset = Estado.objects.all()
    serializer_class = EstadosSerializer


class CidadesViewSet(viewsets.ModelViewSet):
    queryset = Cidade.objects.all()
    serializer_class = CidadesSerializer
    pagination_class = CustomPagination


class CartoriosViewSet(viewsets.ModelViewSet):
    queryset = Cartorio.objects.all()
    serializer_class = CartoriosSerializer


