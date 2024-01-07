from django.urls import path
from .views import hello_api, book_api, books_api, BooksAPI, BookAPI, BooksAPIMixins, BookAPIMixins, BooksAPIGrnerics, \
	BookAPIGenerics

urlpatterns = [
	path('hello/', hello_api),
	path('fbv/books/', books_api),
	path('fbv/book/<int:bid>/', book_api),
	path('cbv/books/', BooksAPI.as_view()),
	path('cbv/book/<int:bid>/', BookAPI.as_view()),
	path('mixin/books/', BooksAPIMixins.as_view()),
	path('mixin/book/<int:bid>/', BookAPIMixins.as_view()),
	path('generic/book/', BooksAPIGrnerics.as_view()),
	path('generic/book/<int:bid>/', BookAPIGenerics.as_view()),
]