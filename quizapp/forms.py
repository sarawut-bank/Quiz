from django import forms
from .models import AllData

class AllDataForm(forms.ModelForm):
    class Meta:
        model = AllData
        fields = '__all__'