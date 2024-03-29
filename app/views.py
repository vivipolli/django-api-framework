from rest_framework.views import APIView
from .filters import PalestraFilter
from rest_framework import generics

from .models import Palestra, Palestrante
from .serializers import PalestraSerializer, PalestranteSerializer



class PalestraListCreate(generics.ListCreateAPIView):
    queryset = Palestra.objects.all()
    serializer_class = PalestraSerializer
    filter_class = PalestraFilter

class PalestraEditDel(generics.RetrieveUpdateDestroyAPIView):
    queryset = Palestra.objects.all()
    serializer_class = PalestraSerializer


class PalestranteListCreate(generics.ListCreateAPIView):
    queryset = Palestrante.objects.all()
    serializer_class = PalestranteSerializer

class PalestranteEditDel(generics.RetrieveUpdateDestroyAPIView):
    queryset = Palestrante.objects.all()
    serializer_class = PalestranteSerializer
