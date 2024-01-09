from django.urls import path
from one_punch.views import TestAPI, CoupangAPI

# todo - rest api url 적용하기.
urlpatterns = [
	# /one_punch/test/get/
	path('test/get/', TestAPI.as_view()),
	# /one_punch/coupang/get/
	path('coupang/get/', CoupangAPI.as_view()),
]