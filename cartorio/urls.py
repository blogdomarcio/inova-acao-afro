from django.urls import path, include

from cartorio import views
from cartorio.api.routers import router


app_name = 'cartorio'

urlpatterns = [
    path('api/', include(router.urls)),
    path('', views.index, name='index'),
    path('estados', views.estados, name='estados'),
    path('estado/<str:estado>/', views.estado, name='estado_detalhe'),
    path('cidade/<int:cidade>', views.cidade, name='cidade'),
    path('cartorio/<int:cartorio>', views.catorio_detalhe, name='catorio_detalhe'),

    path('api/lista-estados', views.lista_estados, name='api-estados'),
    path('api/lista-cidades-estado/<str:estado>', views.lista_cidades_estado, name='api-cidade-estados'),
    path('api/lista-cartorios-cidade/<str:cidade>', views.lista_cartorios_cidade, name='lista_cartorios_cidade'),




]
