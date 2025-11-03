from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def films(request):
    films = {
        'Joker': 7.5,
        'Inception': 8.8,
        'Avatar': 7.8,
        'Interstellar': 9.0,
        'Tenet': 7.3
    }
    return render(request, 'films.html', {'films': films})
