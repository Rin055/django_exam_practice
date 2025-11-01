from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def film_rating(request):
    films = {
        "Inception": 8.8,
        "The Dark Knight": 9.0,
        "Interstellar": 7.6,
        "The Matrix": 8.5,
        "Pulp Fiction": 5.9,
    }
    context = {'films': films}
    return render(request, 'films.html', context)
