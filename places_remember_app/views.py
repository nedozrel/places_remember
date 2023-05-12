from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import DetailView

from places_remember_app.forms import PlaceForm
from places_remember_app.models import Place


def index(request):
    if request.user.is_authenticated:
        return redirect('places')

    return render(request, 'places_remember_app/index.html')


class PlacesView(LoginRequiredMixin, View):
    @staticmethod
    def get_context(request):
        return {
            'places': Place.objects.filter(user=request.user),
            'form': PlaceForm(request.POST) if request.POST else PlaceForm()
        }

    def get(self, request):
        return render(request, 'places_remember_app/place_list.html', self.get_context(request))

    def post(self, request):
        context = self.get_context(request)
        if context['form'].is_valid():
            place = context['form'].save(commit=False)
            place.user = request.user
            print(len(place.title))
            place.save()
            return redirect('places')

        return render(request, 'places_remember_app/place_list.html', context)


class PlaceDetailView(LoginRequiredMixin, DetailView):
    model = Place

    def dispatch(self, request, *args, **kwargs):
        place = self.get_object()
        if place.user != self.request.user:
            raise PermissionDenied('You do not have permission to view this page.')
        return super().dispatch(request, *args, **kwargs)
