from rest_framework.viewsets import ModelViewSet
from book.serializers import BookSerializer,CategorySerializer, AuthorSerializer
from book.models import Book,Category, Author
from api.permissions import IsLibrarianOrReadOnly
from rest_framework.permissions import IsAdminUser,IsAuthenticated

class BooksViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated, IsLibrarianOrReadOnly]

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated, IsLibrarianOrReadOnly]

class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticated, IsLibrarianOrReadOnly]