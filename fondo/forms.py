from django import forms
from .models import SolicitudCredito

class SolicitudesForm(forms.ModelForm):
    model = SolicitudCredito
    fields = ['credito', 'monto_credito', 'plazo_credito', 'documentos_solicitud', 'autoriza_descuento', 'pagare' ]
    widgets = {
        'credito': forms.TextInput(attrs={'class':'form-control mt-1'}),
        'monto_credito': forms.TextInput(attrs={'class':'form-control mt-1'}),
        'plazo_credito': forms.TextInput(attrs={'class':'form-control mt-1'}),
        'documentos_solicitud': forms.ClearableFileInput(attrs={'class':'form-control mt-1'}),
        'autoriza_descuento': forms.ClearableFileInput(attrs={'class':'form-control mt-1'}),
        'pagare': forms.ClearableFileInput(attrs={'class':'form-control mt-1'}),
        'estado_solicitud': forms.TextInput(attrs={'class':'form-control mt-1'})
    }