from django.urls import path
from one_punch.views import TestAPI, CoupangAPI

# todo - rest api url 적용하기.
urlpatterns = [
	path('test/', TestAPI.as_view()),
	# int:id 는 url로 들어오는 id를 int형으로 받겠다는 의미.
	# keyword 를 받으려면 다음과 같이 코드 생성
	path('coupang/get/<str:keyword>/', CoupangAPI.as_view()),
]