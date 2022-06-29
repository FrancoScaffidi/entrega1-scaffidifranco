from django.urls import path
from AppCoder import views

urlpatterns = [
    path('', views.Inicio, name="Inicio"),
    path('Empleados', views.Empleados, name="Empleados"),
    path('Vacantes', views.Vacantes, name="Vacantes"),
    path('Clientes', views.Clientes, name ="Clientes"),
    path('Buscador/', views.Buscador),
]
