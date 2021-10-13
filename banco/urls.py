from django.urls import path

from banco import views

app_name = 'banco'

urlpatterns = [
    path('', views.index, name='index'),
    path('agencias/', views.lista, name='agencias'),
]
