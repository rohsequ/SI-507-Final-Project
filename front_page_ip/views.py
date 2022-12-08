from django.shortcuts import render, redirect
import requests
import json
import os
from django.contrib.auth.decorators import login_required

from .forms import RecommendLocation
from .models import Country,State, City, PersonLocation

from dotenv import load_dotenv

load_dotenv()

@login_required
def person_loc_update_view(request):
    form = RecommendLocation(instance=request.user)
    if request.method == 'POST':
        form = RecommendLocation(request.POST, instance=request.user)

        if form.is_valid():
            print(form.cleaned_data.items())
            personloc = PersonLocation.objects.get(user=request.user)
            personloc.country=form.cleaned_data['country']
            personloc.state=form.cleaned_data['state']
            personloc.city=form.cleaned_data['city']
            personloc.latitude=form.cleaned_data['city'].latitude
            personloc.longitude=form.cleaned_data['city'].longitude
            personloc.save()
            api_key = str(os.getenv('YELP_API_KEY'))
            headers = {'Authorization': 'Bearer %s' % api_key}
            params={'latitude': str(form.cleaned_data['city'].latitude), 'longitude': str(form.cleaned_data['city'].longitude), 'sort_by':'rating', 'limit':'50'}
            url='https://api.yelp.com/v3/businesses/search'
            req=requests.get(url, params=params, headers=headers)
            package = json.loads(req.text)
            package = package['businesses']
            if package:
                return render(request, 'food_cards.html', {'package': package, 'city': form.cleaned_data['city'].name, 'state': form.cleaned_data['state'].name})
            else:
                return render(request, "404_no_recommend.html")
    return render(request, 'loc_home.html', {'form': form})

@login_required
def continue_to_main_view(request):
    personloc = PersonLocation.objects.get(user=request.user)
    api_key = str(os.getenv('YELP_API_KEY'))
    headers = {'Authorization': 'Bearer %s' % api_key}
    params={'latitude': str(personloc.latitude), 'longitude': str(personloc.longitude), 'sort_by':'rating', 'limit':'50'}
    url='https://api.yelp.com/v3/businesses/search'
    req=requests.get(url, params=params, headers=headers)
    package = json.loads(req.text)
    package = package['businesses']
    return render(request, 'food_cards.html', {'package': package})

def load_cities(request):
    state_id = request.GET.get('state_id')
    cities = City.objects.filter(state_id=state_id).all()
    return render(request, 'city_dropdown_list_options.html', {'data': cities})

def load_states(request):
    country_id = request.GET.get('country_id')
    states = State.objects.filter(country_id=country_id).all()
    return render(request, 'city_dropdown_list_options.html', {'data': states})

# Create your views here.
@login_required
def home(request):
    ip = requests.get('https://api.ipify.org?format=json')
    ip_data = json.loads(ip.text)    
    res = requests.get(f'http://ip-api.com/json/{ip_data["ip"]}')
    location_data_one = res.text
    location_data = json.loads(location_data_one)
    if location_data['status'] == "success":
        country_id = Country.objects.get(name = location_data["country"])
        state_id = State.objects.get(name = location_data["regionName"])
        city_id = City.objects.get(name = location_data["city"])
        try:
            personloc = PersonLocation.objects.get(user=request.user)
            personloc.country=country_id
            personloc.state=state_id
            personloc.city=city_id
            personloc.ip_address = ip_data["ip"]
            personloc.latitude=city_id.latitude
            personloc.longitude=city_id.longitude
        except:
            personloc = PersonLocation(user=request.user, country=country_id,state=state_id, city=city_id,
                                ip_address=ip_data["ip"], latitude=city_id.latitude,longitude=city_id.longitude)
        personloc.save()
        return render(request, 'auth_home.html', {'data': location_data})
    else:
        return render(request, 'loc_home.html')
