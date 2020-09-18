from django.urls import path, include
from . import views
from .views import PredictView

urlpatterns = [
	path('api/dt-predict/', PredictView.as_view(), name='decision-tree-predict'),
	path('', views.indexView, name='index')
]