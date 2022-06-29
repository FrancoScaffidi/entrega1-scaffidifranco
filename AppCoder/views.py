from django.shortcuts import render, HttpResponse
from itertools import product
from AppCoder.models import *
from AppCoder.forms import *

def Inicio(request):
    
    return render(request, "AppCoder/Inicio.html")

def Empleados(request):

    if request.method == "POST":

        miFormulario = EmpleadosFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:

            informacion = miFormulario.cleaned_data 

            empleado = Empleados(nombre=informacion["nombre"], apellido=informacion["apellido"], mail=informacion["mail"])

            empleado.save()

            return render(request, "AppCoder/Inicio.html")
    else:

        miFormulario = EmpleadosFormulario()
        
        return render(request, "AppCoder/Empleados.html", {"miFormulario": miFormulario} )


def Vacantes(request):

    if request.method == "POST":

        miFormulario = VacantesFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:
            
            informacion = miFormulario.cleaned_data

            vacante = Vacantes(nombre=informacion["nombre"], apellido=informacion["apellido"], mail=informacion["mail"], dni=informacion["dni"])

            vacante.save()

            return render(request, "AppCoder/Inicio.html")
    else:

        miFormulario = VacantesFormulario()

        return render(request, "AppCoder/Vacantes.html", {"miFormulario": miFormulario})

def Clientes(request):

    if request.method == "POST":

        miFormulario = ClientesFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:

            informacion = miFormulario.cleaned_data

            cliente = Clientes(nombre=informacion["nombre"], apellido=informacion["apellido"])

            cliente.save()

            return render(request, "AppCoder/Inicio.html")
    
    else:

        miFormulario = VacantesFormulario()

        return render(request, "AppCoder/Clientes.html", {"miFormulario": miFormulario})

def Buscador(request):

    if request.GET["nombres"]:
        
        nombres = request.GET["nombres"]

        print(nombres)

        apellido = request.GET["apellido"]

        print(apellido)

        return render(request, "AppCoder/Inicio.html", {"nombres":nombres, "apellido":apellido})
    
    else:

        respuesta = print("No se enviaron datos")
    
    return render (request, "AppCoder/Inicio.html", {"respuesta":respuesta})




# Create your views here.
