from rest_framework import serializers

from core.models import Pessoa, Cargo


class PessoaSerializer(serializers.ModelSerializer):
    cargo = serializers.ReadOnlyField(source='cargo.nome')

    class Meta:
        model = Pessoa
        fields = '__all__'


class CargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cargo
        fields = '__all__'
