from django.urls import path

from web import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.consulta, name='consulta'),
]
