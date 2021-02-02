import json
from django.test import TestCase, Client, tag
from testapi.models import Animal
from django.urls import reverse


# Create your tests here.

class AnimalTest(TestCase):
    def setUp(self) -> None:
        Animal.objects.create(name='lion', sound='roar')
        Animal.objects.create(name='cat', sound='meow')

    def test_animals_can_speak(self):
        lion = Animal.objects.get(name='lion')
        self.assertEqual(lion.speak(), 'The lion says "roar"')


class LoginTest(TestCase):
    @tag('fast')
    def test_login(self):
        url = reverse('testapi:login')
        client = Client()
        response = client.post(path=url, data={'username': 'admin'}, content_type='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), dict(status=True))
