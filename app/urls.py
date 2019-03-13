from django.urls import path
from .views import PalestraListCreate, PalestraEditDel, PalestranteListCreate, PalestranteEditDel


app_name = "app"

urlpatterns = [
    path('palestras/', PalestraListCreate.as_view()),
    path('palestras/<int:pk>', PalestraEditDel.as_view()),
    path('palestrante/', PalestranteListCreate.as_view()),
    path('palestrante/<int:pk>', PalestranteEditDel.as_view())
]
