from rest_framework import serializers

from .models import Palestra, Palestrante


class PalestraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Palestra
        fields = ('id', 'titulo', 'descricao', 'data','hora', 'palestrante')


class PalestranteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Palestrante
        fields = ('id', 'nome', 'bio', 'link')
