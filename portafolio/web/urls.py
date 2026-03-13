from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('paisajes/', views.paisajes, name='paisajes'),
    path('viajes/', views.viajes, name='viajes'),
    path('retratos/', views.retratos, name='retratos'),
    path('vida_silvestre/', views.vida_silvestre, name='vida_silvestre'),
    path('contacto/', views.contacto, name='contacto'),
]