from django.shortcuts import render, redirect

from places_remember_app.forms import PlaceForm


def index(request):
    form = PlaceForm()
    if request.method == 'POST':
        form = PlaceForm(request.POST)
        if form.is_valid():
            place = form.save(commit=False)
            place.user = request.user
            place.save()
        return redirect('index')
    return render(request, 'places_remember_app/index.html', context={'form': form})
