
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from core.api import CargoViewSet, PessoaViewSet

router = routers.DefaultRouter()
router.register(r'pessoas', PessoaViewSet)
router.register(r'cargos', CargoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
