from rest_framework.views import APIView
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics



from .models import Palestra, Palestrante
from .serializers import PalestraSerializer, PalestranteSerializer



class PalestraListCreate(generics.ListCreateAPIView):
    queryset = Palestra.objects.all()
    serializer_class = PalestraSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('data',)

class PalestraEditDel(generics.RetrieveUpdateDestroyAPIView):
    queryset = Palestra.objects.all()
    serializer_class = PalestraSerializer


class PalestranteListCreate(generics.ListCreateAPIView):
    queryset = Palestrante.objects.all()
    serializer_class = PalestranteSerializer

class PalestranteEditDel(generics.RetrieveUpdateDestroyAPIView):
    queryset = Palestrante.objects.all()
    serializer_class = PalestranteSerializer
