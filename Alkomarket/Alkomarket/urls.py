from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='/alko/')),
    path('admin/', admin.site.urls),
    path('alko/', include('alko.urls')),
]