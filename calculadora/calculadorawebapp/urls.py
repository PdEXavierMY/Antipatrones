from django.urls import path
from calculadorawebapp import views

urlpatterns = [
    path('', views.index, name='index'),
]