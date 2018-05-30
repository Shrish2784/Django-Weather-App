from django.forms import ModelForm
from Weather.models import City


class AddCityForm(ModelForm):
    class Meta:
        model = City
        fields = '__all__'
