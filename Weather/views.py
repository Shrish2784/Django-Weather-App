import requests
from django.shortcuts import render
from django.views.generic import FormView
from Weather.models import City
from Weather.forms import AddCityForm


class IndexView(FormView):
    template_name = 'Weather/index.html'
    form_class = AddCityForm
    success_url = '/'

    def form_valid(self, form):
        name = form.cleaned_data['name']
        obj = City.objects.create(name=name.lower())
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context_dict = super().get_context_data(**kwargs)
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=4c82fae2ad4ecd362a50055af2df5a54&units=metric'
        cities = City.objects.all()
        weather = []
        for city in cities:
            res = requests.get(url.format(city.name)).json()
            name_list = city.name.split(' ')
            name = ''
            for word in name_list:
                print(word)
                name += word.capitalize()
                name += ' '
            city_weather = {
                'name': name,
                'temp': res['main']['temp'],
                'desc': res['weather'][0]['description']
            }
            weather.append(city_weather)
        print(weather)
        context_dict['weather'] = weather
        return context_dict
