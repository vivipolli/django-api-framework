from .models import Palestra
import django_filters

class PalestraFilter(django_filters.FilterSet):
    class Meta:
        model = Palestra
        fields = ['data',]
