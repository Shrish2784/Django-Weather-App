from django.forms import ModelForm
from django import forms
from Weather.models import City


class AddCityForm(ModelForm):

    name = forms.CharField(max_length=250)

    def clean(self):
        cleaned_data = super(AddCityForm, self).clean()
        cleaned_data['name'] = cleaned_data['name'].lower()

    class Meta:
        model = City
        fields = '__all__'
