import django_filters

from core.models import Cargo, Pessoa


class CargoFilter(django_filters.FilterSet):
    class Meta:
        model = Cargo
        fields = {
            'nome': ['exact', 'contains'],
        }


class PessoaFilter(django_filters.FilterSet):
    class Meta:
        model = Pessoa
        fields = {
            'nome': ['exact', 'contains'],
            'admissao': ['exact', 'gte', 'lte'],
            'cargo': ['exact']
        }
