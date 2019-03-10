from rest_framework import serializers

from .models import Palestra, Palestrante


class PalestraSerializer(serializers.Serializer):
    titulo = serializers.CharField(max_length=50)
    descricao = serializers.CharField()
    dataHora = serializers.DateTimeField()
    palestrante_id = serializers.IntegerField()

    def create(self, validated_data):
        return Palestra.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.titulo = validated_data.get('titulo', instance.titulo)
        instance.descricao = validated_data.get(
            'descricao', instance.descricao)
        instance.dataHora = validated_data.get('dataHora', instance.dataHora)
        instance.palestrante_id = validated_data.get(
            'palestrante_id', instance.palestrante_id)

        instance.save()
        return instance


class PalestranteSerializer(serializers.Serializer):
    nome = serializers.CharField(max_length=50)
    bio = serializers.CharField()
    link = serializers.URLField()
    palestra_id = serializers.IntegerField()

    def create(self, validated_data):
        return Palestrante.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.nome = validated_data.get('nome', instance.nome)
        instance.bio = validated_data.get(
            'bio', instance.bio)
        instance.link = validated_data.get('link', instance.link)

        instance.save()
        return instance
