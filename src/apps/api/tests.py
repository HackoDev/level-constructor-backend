from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.main.models import Location, Game


class LocationsViewSetTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(is_active=True, username='test',
                                        password='test')
        self.game = Game.objects.create(title='Test', description='')
        self.locations = Location.objects.bulk_create([
            Location(game=self.game, name='Test1', description='',
                     is_start=True, is_finish=False),
            Location(game=self.game, name='Test2', description='',
                     is_start=False, is_finish=False),
            Location(game=self.game, name='Test2', description='',
                     is_start=False, is_finish=True),
        ])
        self.client.force_login(self.user)

    def test_list_endpoint(self):
        list_url = reverse('api:locations-list')
        response = self.client.get(list_url)
        self.assertTrue(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), len(self.locations))

    def test_list_endpoint_filter_by_game(self):
        list_url = reverse('api:locations-list')

        filter_params = {'game': self.game.id}
        queryset = Location.objects.filter(game=filter_params['game'])
        response = self.client.get(list_url, data=filter_params)
        self.assertTrue(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), queryset.count())

    def test_list_endpoint_filter_by_is_start(self):
        list_url = reverse('api:locations-list')

        filter_params = {'is_start': True}
        queryset = Location.objects.filter(is_start=filter_params['is_start'])
        response = self.client.get(list_url, data=filter_params)
        self.assertTrue(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), queryset.count())

    def test_list_endpoint_filter_by_is_end(self):
        list_url = reverse('api:locations-list')

        filter_params = {'is_finish': True}
        queryset = Location.objects.filter(
            is_finish=filter_params['is_finish']
        )
        response = self.client.get(list_url, data=filter_params)
        self.assertTrue(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), queryset.count())

    def test_list_endpoint_filter_by_name(self):
        list_url = reverse('api:locations-list')

        filter_params = {'name': self.locations[0].name}
        queryset = Location.objects.filter(
            name__icontains=filter_params['name']
        )
        response = self.client.get(list_url, data=filter_params)
        self.assertTrue(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), queryset.count())

        filter_params = {'name': 'wrong_name'}
        queryset = Location.objects.filter(
            name__icontains=filter_params['name']
        )
        response = self.client.get(list_url, data=filter_params)
        self.assertTrue(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), queryset.count())
