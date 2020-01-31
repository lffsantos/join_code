import django_filters

from core.models import Cargo


class CargoFilter(django_filters.FilterSet):
    class Meta:
        model = Cargo
        fields = {
            'nome': ['exact', 'contains'],
        }
