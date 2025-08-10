from rest_framework.viewsets import ModelViewSet
from book.serializers import BookSerializer,CategorySerializer, AuthorSerializer
from book.models import Book,Category, Author
from api.permissions import IsLibrarianOrReadOnly
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class BooksViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated, IsLibrarianOrReadOnly]


    @swagger_auto_schema(
    operation_summary="List all books",
    operation_description="Retrieve a list of all books in the library",
    responses={200: BookSerializer(many=True)},
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Retrieve a book",
        operation_description="Get detailed information about a specific book",
        responses={200: BookSerializer},
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Create a new book",
        operation_description="Add a new book to the library. Requires librarian privileges.",
        responses={201: BookSerializer},
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Update a book",
        operation_description="Update all fields of an existing book. Requires librarian privileges.",
        responses={200: BookSerializer},
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Partial update a book",
        operation_description="Update some fields of an existing book. Requires librarian privileges.",
        responses={200: BookSerializer},
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Delete a book",
        operation_description="Delete a book from the library. Requires librarian privileges.",
        responses={204: "Book deleted successfully"},
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
    

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated, IsLibrarianOrReadOnly]


    @swagger_auto_schema(
    operation_summary="List all categories",
    operation_description="Retrieve a list of all categories in the library",
    responses={200: CategorySerializer(many=True)},
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Retrieve a category",
        operation_description="Get detailed information about a specific category",
        responses={200: CategorySerializer},
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Create a new category",
        operation_description="Add a new category to the library. Requires librarian privileges.",
        responses={201: CategorySerializer},
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Update a categories",
        operation_description="Update all fields of an existing category. Requires librarian privileges.",
        responses={200: CategorySerializer},
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Partial update a category",
        operation_description="Update some fields of an existing category. Requires librarian privileges.",
        responses={200: CategorySerializer},
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Delete a category",
        operation_description="Delete a category from the library. Requires librarian privileges.",
        responses={204: "Book deleted successfully"},
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
    

class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticated, IsLibrarianOrReadOnly]


    @swagger_auto_schema(
    operation_summary="List all authors",
    operation_description="Retrieve a list of all authors in the library",
    responses={200: BookSerializer(many=True)},
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Retrieve a author",
        operation_description="Get detailed information about a specific author",
        responses={200: AuthorSerializer},
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Create a new author",
        operation_description="Add a new author to the library. Requires librarian privileges.",
        responses={201: AuthorSerializer},
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Update a author",
        operation_description="Update all fields of an existing author. Requires librarian privileges.",
        responses={200: AuthorSerializer},
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Partial update a author",
        operation_description="Update some fields of an existing author. Requires librarian privileges.",
        responses={200: AuthorSerializer},
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Delete a author",
        operation_description="Delete a author from the library. Requires librarian privileges.",
        responses={204: "Book deleted successfully"},
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
