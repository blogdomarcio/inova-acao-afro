from django.urls import path

from peoples import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pessoas', views.lista, name='lista'),
    path('pessoa/detalhe/<str:codigo>', views.detalhe, name='detalhe'),
    # path('consulta', views.consulta, name='consulta'),

]
