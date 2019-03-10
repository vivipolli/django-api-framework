from django.urls import path
from .views import PalestraView, PalestranteView


app_name = "app"

urlpatterns = [
    path('palestra/', PalestraView.as_view()),
    path('palestra/<int:pk>', PalestraView.as_view()),
    path('palestrante/', PalestranteView.as_view()),
    path('palestrante/<int:pk>', PalestranteView.as_view())
]
