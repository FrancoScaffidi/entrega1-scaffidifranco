from django import forms


class EmpleadosFormulario(forms.Form):
    
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    mail = forms.EmailField()


class VacantesFormulario(forms.Form):
    
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    mail = forms.EmailField()
    dni = forms.IntegerField()


class ClientesFormulario(forms.Form):
    
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)             #Clases
    