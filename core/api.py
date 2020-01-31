import json

from django.db.models import Sum, Count
from django.http import JsonResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter

from core.filters import CargoFilter, PessoaFilter
from core.models import Pessoa, Cargo
from core.serializers import PessoaSerializer, CargoSerializer


class PessoaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_class = PessoaFilter
    

class CargoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_class = CargoFilter


def total_por_cargo(request):
    cargos = Pessoa.objects.values('cargo__nome').annotate(total=Count('cargo')).order_by('-total')
    result = []
    for cargo in cargos:
        result.append({
            'nome': cargo['cargo__nome'],
            'total': cargo['total']
        })
    if result:
        status = 200
    else:
        status = 404

    return JsonResponse(json.dumps(result), safe=False, status=status)


def mais_antigo(request):
    funcionario = Pessoa.objects.select_related('cargo').all().order_by('admissao').values('nome', 'cargo__nome').first()
    result = {}
    if funcionario:
        result = {
            'nome': funcionario['nome'],
            'cargo': funcionario['cargo__nome']
        }
        status = 200
    else:
        status = 404

    return JsonResponse(result, status=status)
