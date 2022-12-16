from django import forms
from .models import Chart

class ChartForm(forms.ModelForm):
    class Meta:
        model = Chart
        fields = '__all__'
        widgets = {
            'name_y': forms.TextInput(attrs={'class': 'form-control'}),
            'num_x': forms.TextInput(attrs={'class': 'form-control'})
        }