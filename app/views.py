from django.shortcuts import get_object_or_404
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Palestra, Palestrante
from .serializers import PalestraSerializer, PalestranteSerializer


class PalestraView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'home.html'

    def get(self, request):
        palestras = Palestra.objects.all()
        serializer = PalestraSerializer(palestras, many=True)
        return Response({"palestras": palestras, "serializer": serializer})

    def post(self, request):
        palestra = request.data.get('palestra')
        serializer = PalestraSerializer(data=palestra)
        if serializer.is_valid(raise_exception=True):
            palestra_saved = serializer.save()
        return Response({"success": "Palestra '{}' criada com sucesso".format(palestra_saved.titulo)})

    def put(self, request, pk):
        saved_palestra = get_object_or_404(Palestra.objects.all(), pk=pk)
        data = request.data.get('palestra')
        serializer = PalestraSerializer(
            instance=saved_palestra, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            palestra_saved = serializer.save()
        return Response({"success": "Palestra '{}' atualizada com sucesso".format(palestra_saved.title)})

    def delete(self, request, pk):
        palestra = get_object_or_404(Palestra.objects.all(), pk=pk)
        palestra.delete()
        return Response({"message": "Palestra com id `{}` foi deletado.".format(pk)}, status=204)


class PalestranteView(APIView):
    # renderer_classes = [TemplateHTMLRenderer]
    # template_name = 'home.html'

    def get(self, request):
        palestrantes = Palestrante.objects.all()
        serializer = PalestranteSerializer(palestrantes, many=True)
        return Response({"palestrantes": palestrantes, "serializer": serializer})

    def post(self, request):
        palestrante = request.data.get('palestrante')
        serializer = PalestranteSerializer(data=palestrante)
        if serializer.is_valid(raise_exception=True):
            palestrante_saved = serializer.save()
        return Response({"success": "Palestrante '{}' criado com sucesso".format(palestrante_saved.titulo)})

    def put(self, request, pk):
        saved_palestrante = get_object_or_404(Palestrante.objects.all(), pk=pk)
        data = request.data.get('palestrante')
        serializer = PalestranteSerializer(
            instance=saved_palestrante, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            palestrante_saved = serializer.save()
        return Response({"success": "Palestrante '{}' atualizado com sucesso".format(palestrante_saved.title)})

    def delete(self, request, pk):
        palestrante = get_object_or_404(Palestrante.objects.all(), pk=pk)
        palestrante.delete()
        return Response({"message": "Palestrante com id `{}` foi deletado.".format(pk)}, status=204)
