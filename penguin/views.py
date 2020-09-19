from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from ML.decisionTree import DecisionTreeClassifier
import json

# Create your views here.

def indexView(request):
	return render(request, 'penguin/index.html', {})

class PredictView(APIView):

	permission_classes = (permissions.AllowAny,)
    http_method_names = ['get', 'head', 'post']

    def get(self, request, format=None):
    	return Response({"example-data": {
				'island': 'Torgersen',
				'bill_length_mm': 50,
				'bill_depth_mm': 15,
				'flipper_length_mm': 200,
				'body_mass_g': 4500,
				'sex': 'female'
			}})

	def post(self, request, format=None):
		try:
			model = DecisionTreeClassifier()
			print(request.data)
			data = model.predict(request.data)
		except Exception as e:
			return Response({'error': e})
		return Response(data)