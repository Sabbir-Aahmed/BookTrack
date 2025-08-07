from rest_framework.viewsets import ModelViewSet
from book.serializers import BookSerializer,CategorySerializer, AuthorSerializer
from book.models import Book,Category, Author


class BooksViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer