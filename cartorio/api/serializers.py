from rest_framework import serializers

from cartorio.models import Estado, Cidade, Cartorio


class EstadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estado
        fields = '__all__'


class CidadesSerializer(serializers.ModelSerializer):
    uf = serializers.StringRelatedField(many=False)
    class Meta:
        model = Cidade
        fields = ('id', 'nome', 'uf')

class CartoriosSerializer(serializers.ModelSerializer):
    cidade = serializers.StringRelatedField(many=False)
    bairro = serializers.StringRelatedField(many=False)
    class Meta:
        model = Cartorio
        fields = '__all__'