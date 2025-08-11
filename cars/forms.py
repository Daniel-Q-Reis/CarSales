from django import forms
from cars.models import Car

class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'

    
    def clean_value(self):
        value = self.cleaned_data.get('value')
        if value < 5000:
            self.add_error('value', 'The car value must be higher than $5,000')
        return value