
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from rest_framework import routers

from core.api import CargoViewSet, PessoaViewSet, total_por_cargo, mais_antigo

router = routers.DefaultRouter()
router.register(r'pessoas', PessoaViewSet)
router.register(r'cargos', CargoViewSet)

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html')),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('total-por-cargo/', total_por_cargo),
    path('mais-antigo/', mais_antigo),
]
