from django import forms
from .models import Medicamento

class MedicamentoForm(forms.ModelForm):
    class Meta:
        model = Medicamento
        fields = [
            'nombre', 
            'laboratorio', 
            'precio', 
            'stock', 
            'descripcion', 
            'requiere_receta', 
            'fecha_vencimiento'
        ]
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Paracetamol 500mg'}),
            'laboratorio': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Laboratorio Chile'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'requiere_receta': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'fecha_vencimiento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }