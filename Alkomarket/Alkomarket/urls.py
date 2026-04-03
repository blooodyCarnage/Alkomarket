from django.contrib import admin
from django.urls import path, include, register_converter
from alko.converters import FourDigitYearConverter
from django.views.generic import RedirectView

# Регистрируем конвертер с проверкой
try:
    register_converter(FourDigitYearConverter, "year4")
except ValueError:
    pass  # уже зарегистрирован

urlpatterns = [
    path('', RedirectView.as_view(url='/alko/')),
    path('admin/', admin.site.urls),
    path('alko/', include('alko.urls')),
]