from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .forms import NewPlaceForm
import random


def place_list(request):
    return render(request, 'place_list.html', {'place_to_go': request.session.get('places', [])})

def add_place_form(request):
    if request.method == 'POST':
        form = NewPlaceForm(request.POST)
        if form.is_valid():
            place_name = form.cleaned_data['place']
            place_priority = form.cleaned_data['priority']
            if 'places' not in request.session:
                request.session['places'] = []
            request.session['places'].append((place_name, place_priority))
            request.session['places'].sort(key=lambda x: x[1], reverse=True)
            print(request.session['places'])
            request.session.modified = True
            return HttpResponseRedirect(reverse('place_to_go:place_list'))
        else:
            return render(request, 'add_place.html', {'form':form})
    return render(request, 'add_place.html', {'form': NewPlaceForm()})

def home_page(request):
    user_places = request.session.get('places', [])
    if not user_places:
        context = {
            "selected_place": None,
            "selected_priority": None,
        }
        return render(request, 'home_page.html', context)
    weight = sum(place[1] for place in user_places)
    random_choice = random.randrange(0, weight)
    cumulative_weight = 0
    selected_place = None
    for place in user_places:
        cumulative_weight += place[1]
        if random_choice <= cumulative_weight:
            selected_place = place
            break
    context = {"selected_place": selected_place[0] if selected_place else None,
               "selected_priority": selected_place[1] if selected_place else None,}
    
    return render(request, 'home_page.html', context)
