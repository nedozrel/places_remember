# pylint: disable=imported-auth-user
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from places_remember_app.models import Place
from places_remember_app.forms import PlaceForm


class IndexViewTestCase(TestCase):
    def test_index_view_not_authenticated(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'places_remember_app/index.html')

    def test_index_view_authenticated(self):
        user = User.objects.create_user(username='testuser', password='testpass')
        self.client.force_login(user)
        response = self.client.get(reverse('index'))
        self.assertRedirects(response, reverse('places'))


class PlacesViewTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.force_login(self.user)
        self.place = Place.objects.create(
            title='Test Place',
            description='This is a test place',
            longitude=1.0,
            latitude=1.0,
            user=self.user
        )

    def test_places_view_get(self):
        response = self.client.get(reverse('places'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'places_remember_app/place_list.html')
        self.assertContains(response, self.place.title)
        self.assertIsInstance(response.context['form'], PlaceForm)

    def test_places_view_post(self):
        data = {
            'title': 'New Test Place',
            'description': 'This is a new test place',
            'longitude': 2.0,
            'latitude': 2.0,
        }
        response = self.client.post(reverse('places'), data=data)
        self.assertRedirects(response, reverse('places'))
        self.assertTrue(Place.objects.filter(title=data['title']).exists())

    def test_places_view_post_invalid_form(self):
        data = {
            'title': '',
            'description': 'This is an invalid form',
            'longitude': 2.0,
            'latitude': 2.0,
        }
        response = self.client.post(reverse('places'), data=data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'This field is required')
        self.assertFalse(Place.objects.filter(description=data['description']).exists())


class PlaceDetailViewTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.force_login(self.user)
        self.place = Place.objects.create(
            title='Test Place',
            description='This is a test place',
            longitude=1.0,
            latitude=1.0,
            user=self.user
        )

    def test_place_detail_view_authenticated_owner(self):
        response = self.client.get(reverse('places_detail', args=[self.place.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'places_remember_app/place_detail.html')
        self.assertEqual(response.context['object'], self.place)

    def test_place_detail_view_authenticated_not_owner(self):
        user2 = User.objects.create_user(username='testuser2', password='testpass')
        self.client.force_login(user2)
        response = self.client.get(reverse('places_detail', args=[self.place.id]))
        self.assertEqual(response.status_code, 403)

    def test_place_detail_view_not_authenticated(self):
        self.client.logout()
        response = self.client.get(reverse('places_detail', args=[self.place.id]))
        self.assertEqual(response.status_code, 403)
