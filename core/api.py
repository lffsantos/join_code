from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter

from core.filters import CargoFilter
from core.models import Pessoa, Cargo
from core.serializers import PessoaSerializer, CargoSerializer


class PessoaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = []


class CargoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_class = CargoFilter
