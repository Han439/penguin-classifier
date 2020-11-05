from django.test import SimpleTestCase
from rest_framework.test import APIClient

# Create your tests here.


class TestViews(SimpleTestCase):

    def test_index_view(self):
        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'penguin/index.html')

    def test_predict_view_GET(self):
        client = APIClient()
        response = client.get('/api/dt-predict/')
        self.assertEqual(response.status_code, 200)

    def test_predict_view_POST_with_valid_payload(self):
        client = APIClient()
        input_data = {
            'island': 'Torgersen',
            'bill_length_mm': 50,
            'bill_depth_mm': 15,
            'flipper_length_mm': 200,
            'body_mass_g': 4500,
            'sex': 'female'
        }

        predict_url = "/api/dt-predict/"
        response = client.post(predict_url, input_data, format='json')

        self.assertEqual(response.status_code, 200)
        self.assertIn('result', response.data)
