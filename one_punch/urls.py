from django.urls import path
from one_punch.views import TestAPI

urlpatterns = [
	path('test/', TestAPI.as_view()),
]