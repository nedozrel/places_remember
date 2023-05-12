from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView

from places_remember_app.forms import PlaceForm
from places_remember_app.models import Place


def index(request):
    if request.user.is_authenticated:
        return redirect('places')

    return render(request, 'places_remember_app/index.html')


class PlacesView(LoginRequiredMixin, ListView): # pylint: disable=too-many-ancestors
    model = Place

    def get_queryset(self):
        return Place.objects.filter(user=self.request.user)

    def post(self, request):
        form = PlaceForm(request.POST)
        if form.is_valid():
            place = form.save(commit=False)
            place.user = request.user
            place.save()

        return redirect('places')


class PlaceDetailView(LoginRequiredMixin, DetailView):
    model = Place

    def dispatch(self, request, *args, **kwargs):
        place = self.get_object()
        if place.user != self.request.user:
            raise PermissionDenied("You do not have permission to view this page.")
        return super().dispatch(request, *args, **kwargs)
