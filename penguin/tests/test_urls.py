from django.test import SimpleTestCase
from django.urls import reverse, resolve

from .. import views


# Create your tests here.


class TestUrlsNameResolve(SimpleTestCase):

    def test_index_url_resolve(self):
        url = reverse('index')
        self.assertEqual(resolve(url).func, views.indexView)

    def test_create_poll_url_resolve(self):
        url = '/api/dt-predict/'
        self.assertEqual(resolve(url).func.view_class, views.PredictView)
