from django import forms

from places_remember_app.models import Place


class PlaceForm(forms.ModelForm):
    longitude = forms.DecimalField(
        widget=forms.TextInput(attrs={
            'type': 'hidden',
            'class': 'longitude-input'
        }))
    latitude = forms.DecimalField(
        widget=forms.TextInput(attrs={
            'type': 'hidden',
            'class': 'latitude-input'
        }))

    class Meta:
        model = Place
        fields = ('title', 'description', 'longitude', 'latitude')
