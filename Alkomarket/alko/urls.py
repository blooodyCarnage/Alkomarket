from django.urls import path, register_converter
from alko import views
from alko import converters



urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('cats/<slug:cat_slug>/', views.categories_by_slug, name='cats'),
    path('archive/<int:year>/', views.archive, name='archive'),
    path('post/<int:post_id>/', views.show_post, name='post'),  # добавьте эту строку
]