from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from ML.decisionTree import DecisionTreeClassifier

# Create your views here.

def indexView(request):
	return render(request, 'penguin/index.html', {})

class PredictView(APIView):

	def post(self, request, format=None):
		try:
			model = DecisionTreeClassifier()
			data = model.predict(request.data)
		except Exception as e:
			return Response({'error': e})
		return Response(data)