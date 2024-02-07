from django import forms 

class PlantaForm(forms.Form):
    nombre = forms.CharField(max_length=50,required=True,label="Nombre de la Planta")
    ambiente = forms.CharField(max_length=50,required=True,label="Ambiente de Ubicación")
    riego = forms.CharField(max_length=50,required=True,label="Tipo de Riego")
    iluminacion = forms.CharField(max_length=50,required=True,label="Iluminación")
    tamaño = forms.CharField(max_length=50,required=True,label="Tamaño de la Planta") 

class MacetaForm(forms.Form):
    material = forms.CharField(max_length=50,required=True,label="Material de la Maceta")
    forma = forms.CharField(max_length=50,required=True,label="Forma")
    tamaño = forms.CharField(max_length=50,required=True,label="Tamaño")
    color = forms.CharField(max_length=50,required=True,label="Color")

class FertilizanteForm(forms.Form):
    nombre = forms.CharField(max_length=50,required=True,label="Nombre del Fertilizante")
    nutrientes = forms.CharField(max_length=100,required=True,label="Nutrientes")
    dosis = forms.CharField(max_length=100,required=True,label="Dosis")
    precauciones = forms.CharField(max_length=500,required=True,label="Precauciones")

