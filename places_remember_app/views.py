from django.shortcuts import render


def index(request):
    return render(request, 'places_remember_app/index.html')
