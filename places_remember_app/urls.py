from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('places/', views.PlacesView.as_view(), name='places'),
    path('places/<int:pk>/', views.PlaceDetailView.as_view(), name='places_detail')
]
