from django.urls import path
from . import views  

urlpatterns = [
    path('', views.index, name='index'),
    path('habitat/', views.habitat, name='habitat'),
    path('comportamiento/', views.comportamiento, name='comportamiento'),
    path('impacto/', views.impacto, name='impacto'),
    path('formulario/', views.formulario, name='formulario'),
]
