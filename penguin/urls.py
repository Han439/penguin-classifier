from django.urls import path, include
from . import views

urlpatterns = [
	path('api/dt-predict/', views.PredictView.as_view(), name='decision-tree-predict'),
	path('', views.indexView, name='index')
]