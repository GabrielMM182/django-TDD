from urllib.request import Request
from django.http import request, response
from django.test import RequestFactory, TestCase
from django.urls import reverse
from animais.views import index

class AnimaisURLSTestCase(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    def test_rota_url_utiliza_view_index(self):
        """Teste se a home da aplicação utiliza a função index da views e se ocorrer o http 200 significa que passou corretamente"""
        request = self.factory.get('/')
        response = index(request)
        self.assertEqual(response.status_code, 200)
