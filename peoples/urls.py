from django.urls import path

from peoples import views

app_name = 'pessoas'

urlpatterns = [
    path('', views.index, name='index'),
    path('lista', views.lista, name='lista'),
    path('lista/homens', views.lista_homens, name='lista_homens'),
    path('lista/mulheres', views.lista_mulheres, name='lista_mulheres'),
    path('pessoa/detalhe/<str:codigo>', views.detalhe, name='detalhe'),
    path('pessoa/excluir/<str:codigo>', views.excluir, name='excluir'),

    path('busca', views.busca, name='busca'),

    path('relatorios', views.relatorios, name='relatorios'),
    path('relatorios/maisvelhas', views.maisvelhas, name='maisvelhas'),
    path('relatorios/maisnovas', views.maisnovas, name='maisnovas'),

    path('api/pessoa/json/<str:codigo>', views.json, name='json'),
    path('api/maisvelhas/json/', views.json_maisvelhas, name='json_maisvelhas'),
    path('api/maisnovas/json/', views.json_maisnovas, name='json_maisnovas'),



]
