from django.urls import path

from web import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.curiculo, name='curiculo'),
    path('consulta', views.consulta, name='consulta'),

]
