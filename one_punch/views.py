from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from one_punch.models import TestData
from one_punch.serializers import BookSerializer


class TestAPI(APIView):
	def get(self, request):
		test_data = TestData.objects.all()
		serializer = BookSerializer(test_data, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)

	def post(self, request):
		serializer = BookSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)

		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

