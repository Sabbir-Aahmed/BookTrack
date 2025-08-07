from rest_framework import serializers
from book.models import Book,Category,Author

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            'id','title', 'ISBN', 'author', 'category', 'is_available'
        ]

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id', 'name', 'description'
        ]

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = [
            'id', 'name', 'biography'
        ]

        