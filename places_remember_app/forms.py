from django import forms

from places_remember_app.models import Place


class PlaceForm(forms.ModelForm):
    # pylint: disable=too-few-public-methods
    class Meta:
        model = Place
        fields = ('title', 'description', 'longitude', 'latitude')
