from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from one_punch.engine import CoupangEngine
from one_punch.models import TestData
from one_punch.serializers import BookSerializer


class TestAPI(APIView):
	# def get(self, request):
	# 	test_data = TestData.objects.all()
	# 	serializer = BookSerializer(test_data, many=True)
	# 	return Response(serializer.data, status=status.HTTP_200_OK)

	def get(self, request):
		test_data = 55
		# serializer = BookSerializer(test_data, many=True)
		return Response(test_data, status=status.HTTP_200_OK)

	def post(self, request):
		serializer = BookSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)

		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TotalAPI(APIView):
	pass


class CoupangAPI(APIView):

	def get(self, request, keyword):
		coupang = CoupangEngine(keyword)
		coupang.create_data()
		return Response([coupang.data], status=status.HTTP_200_OK)


class NaverAPI(APIView):
	pass


class DanawaAPI(APIView):
	pass


class EstreetAPI(APIView):
	pass

