"""inovacao_afro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from django.conf.urls.static import static
from django.urls import path, include

from django.contrib.auth import views as auth_views

from inovacao_afro import settings


urlpatterns = [


    path('api-auth/', include('rest_framework.urls')),
    path('admin/', include('smuggler.urls')),  # before admin url patterns!
    path('admin/', admin.site.urls),
    path('', include('web.urls')),
    path('pessoas/', include('peoples.urls')),
    path('banco/', include('banco.urls')),
    path('cartorios/', include('cartorio.urls')),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), {'next_page': '/'}, name='logout'),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

