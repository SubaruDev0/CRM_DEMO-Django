# apps/clients/forms.py 
from django import forms
from .models import Client, Report, ReportFile

class ClientForm(forms.ModelForm):
    """Formulario para crear/editar clientes"""
    class Meta:
        model = Client
        fields = ['name', 'email', 'phone']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre completo del cliente'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'cliente@email.com'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '+56 9 1234 5678'
            }),
        }

class ReportForm(forms.ModelForm):
    """Formulario para crear/editar reportes"""
    class Meta:
        model = Report
        fields = ['title', 'description', 'client']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Título del reporte'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Descripción del reporte...'
            }),
            'client': forms.Select(attrs={'class': 'form-control'}),
        }

class ReportFileForm(forms.ModelForm):
    """Formulario para subir archivos a reportes"""
    class Meta:
        model = ReportFile
        fields = ['file']
        widgets = {
            'file': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': '.pdf,.doc,.docx,.jpg,.jpeg,.png,.txt'  # Tipos permitidos
            })
        }

# Formset para subir múltiples archivos a la vez
ReportFileFormSet = forms.inlineformset_factory(
    Report, 
    ReportFile, 
    form=ReportFileForm,
    extra=3,  # 3 campos para archivos por defecto
    can_delete=True  # Permitir eliminar archivos existentes
)