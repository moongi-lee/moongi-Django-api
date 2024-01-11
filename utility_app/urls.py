from django.urls import path
from utility_app.views import RandomNumberAPI

# todo - rest api url 적용하기.
urlpatterns = [
	# localhost:8000/utility_app/random/num/
	path('random/num/', RandomNumberAPI.as_view()),
]