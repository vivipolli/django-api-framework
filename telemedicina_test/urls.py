from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/', include('app.urls')),
# ]
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view=TemplateView.as_view(template_name='app/home.html')),
]
