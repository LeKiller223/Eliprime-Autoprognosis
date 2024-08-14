from django import forms
from .models import CarScanner, CarModel


class EngineIssueForm(forms.ModelForm):
    car = forms.ModelChoiceField(queryset=CarModel.objects.all())

    class Meta:
        model = CarScanner
        fields = ["car", "symptoms"]
