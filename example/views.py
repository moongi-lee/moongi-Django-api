from rest_framework import viewsets, permissions, generics, status, mixins
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from example.models import Book
from example.serializers import BookSerializer


@api_view(['GET'])
def hello_api(request):
	return Response("Hello World!")


@api_view(['GET', 'POST'])
def books_api(request):
	if request.method == 'GET':
		books = Book.objects.all()
		serializer = BookSerializer(books, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)
	elif request.method == 'POST':
		serializer = BookSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)

		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def	book_api(request, bid):
	book = get_object_or_404(Book, bid=bid)
	serializer = BookSerializer(book)
	return Response(serializer.data, status=status.HTTP_200_OK)


class BooksAPI(APIView):
	def get(self, request):
		books = Book.objects.all()
		serializer = BookSerializer(books, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)

	def post(self, request):
		serializer = BookSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)

		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request):
		Book.objects.all().delete()
		return Response(status=status.HTTP_204_NO_CONTENT)


class BookAPI(APIView):
	def get(self, request, bid):
		book = get_object_or_404(Book, bid=bid)
		serializer = BookSerializer(book)
		return Response(serializer.data, status=status.HTTP_200_OK)

	def put(self, request, bid):
		book = get_object_or_404(Book, bid=bid)
		serializer = BookSerializer(book, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_200_OK)

		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, bid):
		book = get_object_or_404(Book, bid=bid)
		book.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)


class BooksAPIMixins(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
	serializer_class = BookSerializer
	queryset = Book.objects.all()

	def get(self, request, *args, **kwargs):
		return self.list(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)


class BookAPIMixins(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
	serializer_class = BookSerializer
	queryset = Book.objects.all()
	lookup_field = 'bid'

	def get(self, request, *args, **kwargs):
		return self.retrieve(request, *args, **kwargs)

	def put(self, request, *args, **kwargs):
		return self.update(request, *args, **kwargs)

	def delete(self, request, *args, **kwargs):
		return self.destroy(request, *args, **kwargs)


class BooksAPIGrnerics(generics.ListCreateAPIView):
	serializer_class = BookSerializer
	queryset = Book.objects.all()


class BookAPIGenerics(generics.RetrieveUpdateDestroyAPIView):
	serializer_class = BookSerializer
	queryset = Book.objects.all()
	lookup_field = 'bid'