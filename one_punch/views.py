from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from one_punch.engine import CoupangEngine, TestEngine
from one_punch.models import TestData
from one_punch.serializers import BookSerializer


class TestAPI(APIView):
	def get(self, request):
		keyword = "default"
		if request.query_params.get("keyword"):
			keyword = request.query_params.get("keyword")
		else:
			return Response("keyword를 입력해주세요.", status=status.HTTP_400_BAD_REQUEST)

		new_test_engine = TestEngine(keyword)
		new_test_engine.create_data()

		return Response(new_test_engine.data, status=status.HTTP_200_OK)


class TotalAPI(APIView):
	pass


class CoupangAPI(APIView):

	def get(self, request):
		keyword = "default"
		if request.query_params.get("keyword"):
			keyword = request.query_params.get("keyword")
		else:
			return Response("keyword를 입력해주세요.", status=status.HTTP_400_BAD_REQUEST)

		coupang = CoupangEngine(keyword)
		coupang.create_data()
		return Response(coupang.data, status=status.HTTP_200_OK)


class NaverAPI(APIView):
	pass


class DanawaAPI(APIView):
	pass


class EstreetAPI(APIView):
	pass
