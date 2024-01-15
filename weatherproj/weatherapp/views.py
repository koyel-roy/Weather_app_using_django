from django.shortcuts import render
import requests
from .models import City
from . forms import CityForm

def index(request):
    cities = City.objects.all()
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=6da2b6f0a7950abcc5363def90bfde7a'
    
    
    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()
        
    
    
    form = CityForm()
    weather_data = []
    for city in cities:
        city_weather = requests.get(url.format(city)).json()
    
        weather = {
            'city':city,
            'temperature':city_weather['main']['temp'],
            'description':city_weather['weather'][0]['description'],
            'icon':city_weather['weather'][0]['icon']
        }
        
        weather_data.append(weather)
    context = {'weather_data': weather_data, 'form' : form}
    return render(request, 'weatherapp/index.html',context) #returns index.html template

