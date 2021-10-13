from rest_framework import routers

from cartorio.api.viewsets import EstadosViewSet, CidadesViewSet, CartoriosViewSet

router = routers.DefaultRouter()
router.register(r'estados', EstadosViewSet)
router.register(r'cidades', CidadesViewSet)
router.register(r'cartorios', CartoriosViewSet)