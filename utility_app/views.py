from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.


class RandomNumberAPI(APIView):

	def get(self, request):
		from random import random
		number = int(random() * 100)
		return Response(number, status=status.HTTP_200_OK)