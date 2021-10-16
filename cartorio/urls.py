from django.urls import path, include

from cartorio import views
from cartorio.api.routers import router
from cartorio.views import lista_cartorios_estado

app_name = 'cartorio'

urlpatterns = [
    path('api/', include(router.urls)),
    path('dashboard/', views.index, name='index'),
    path('estados/', views.estados, name='estados'),
    path('cidades/', views.cidades, name='cidades'),
    path('cartorios/', views.cartorios, name='cartorios'),
    path('estado/<str:estado>/', views.estado, name='estado_detalhe'),
    path('cidade/<int:cidade>', views.cidade, name='cidade'),
    path('cartorio/<int:cartorio>', views.catorio_detalhe, name='catorio_detalhe'),

    path('', views.add_cartorio, name='add-cartorio'),
    path('<int:cartorio>', views.api_cartorio, name='api-cartorio'),
    path('<str:estado>', views.lista_cartorios_estado, name='api-cidade-estados'),
    path('lista-estados', views.lista_estados, name='api-estados'),
    path('lista-cartorios-cidade/<str:cidade>', views.lista_cartorios_cidade, name='lista_cartorios_cidade'),
    path('lista-cidadas-estado/<str:estado>', views.lista_cidades_estado, name='lista_cartorios_estado'),




]
